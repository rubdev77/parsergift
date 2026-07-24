import asyncpg
import logging
from config import DATABASE_URL
import os
import asyncio

logger = logging.getLogger(__name__)

# Global connection pool
pool = None

async def init_db():
    global pool
    # Connect to PostgreSQL using the DATABASE_URL
    pool = await asyncpg.create_pool(DATABASE_URL)
    
    async with pool.acquire() as db:
        # Create users table
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                username TEXT,
                total_gifts INTEGER DEFAULT 0,
                rating INTEGER DEFAULT 0,
                last_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create market history table
        await db.execute('''
            CREATE TABLE IF NOT EXISTS market_history (
                id SERIAL PRIMARY KEY,
                item_name TEXT,
                user_id BIGINT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Create target gifts table
        await db.execute('''
            CREATE TABLE IF NOT EXISTS target_gifts (
                gift_id BIGINT PRIMARY KEY
            )
        ''')

        # Drop old access control table to migrate to new timestamp-based schema
        await db.execute('DROP TABLE IF EXISTS access_control')
        
        # Create new access control table
        await db.execute('''
            CREATE TABLE access_control (
                user_id BIGINT PRIMARY KEY,
                expires_at TIMESTAMP
            )
        ''')
        
    logger.info("Database initialized successfully.")
    
    # Pre-populate with config if empty
    from config import TARGET_GIFT_IDS
    gifts = await get_target_gifts()
    if not gifts and TARGET_GIFT_IDS:
        for gid in TARGET_GIFT_IDS:
            await add_target_gift(gid)

async def add_market_item(user_id: int, username: str, item_name: str):
    """Writes a new lot to history, updating the user if necessary."""
    async with pool.acquire() as db:
        # Insert or ignore user
        await db.execute('''
            INSERT INTO users (user_id, username) 
            VALUES ($1, $2)
            ON CONFLICT(user_id) DO UPDATE SET username=EXCLUDED.username
        ''', user_id, username)
        
        # Insert lot history
        await db.execute('''
            INSERT INTO market_history (user_id, item_name)
            VALUES ($1, $2)
        ''', user_id, item_name)

async def get_user_recent_lots_count(user_id: int, time_window_minutes: int) -> int:
    """Returns the number of lots the user has listed in the last `time_window_minutes`."""
    async with pool.acquire() as db:
        result = await db.fetchval('''
            SELECT COUNT(*) FROM market_history 
            WHERE user_id = $1 
            AND timestamp >= NOW() - make_interval(mins => $2)
        ''', user_id, time_window_minutes)
        return result or 0

async def update_user_metrics(user_id: int, total_gifts: int, rating: int):
    """Updates the scraped metrics for a user."""
    async with pool.acquire() as db:
        await db.execute('''
            UPDATE users
            SET total_gifts = $1, rating = $2, last_checked = CURRENT_TIMESTAMP
            WHERE user_id = $3
        ''', total_gifts, rating, user_id)

async def get_user(user_id: int):
    """Retrieves a user by ID."""
    async with pool.acquire() as db:
        row = await db.fetchrow('SELECT * FROM users WHERE user_id = $1', user_id)
        return dict(row) if row else None

async def get_target_gifts():
    async with pool.acquire() as db:
        rows = await db.fetch('SELECT gift_id FROM target_gifts')
        return [row['gift_id'] for row in rows]

async def add_target_gift(gift_id: int):
    async with pool.acquire() as db:
        await db.execute('INSERT INTO target_gifts (gift_id) VALUES ($1) ON CONFLICT DO NOTHING', gift_id)

async def remove_target_gift(gift_id: int):
    async with pool.acquire() as db:
        await db.execute('DELETE FROM target_gifts WHERE gift_id = $1', gift_id)

# --- Access Control Functions ---

async def grant_access(user_id: int, hours: int):
    async with pool.acquire() as db:
        await db.execute('''
            INSERT INTO access_control (user_id, expires_at)
            VALUES ($1, NOW() + make_interval(hours => $2))
            ON CONFLICT(user_id) DO UPDATE SET expires_at=EXCLUDED.expires_at
        ''', user_id, hours)

async def revoke_access(user_id: int):
    async with pool.acquire() as db:
        await db.execute('DELETE FROM access_control WHERE user_id = $1', user_id)

async def get_access(user_id: int):
    """Returns dict with expires_at if user has access, else None."""
    async with pool.acquire() as db:
        row = await db.fetchrow('SELECT expires_at FROM access_control WHERE user_id = $1', user_id)
        return dict(row) if row else None

async def get_active_users():
    """Returns a list of user_ids that currently have active access."""
    async with pool.acquire() as db:
        rows = await db.fetch('SELECT user_id FROM access_control WHERE expires_at > NOW()')
        return [row['user_id'] for row in rows]
