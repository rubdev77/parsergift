import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API credentials (for Pyrogram userbots)
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "test_hash")

# Bot credentials
BOT_TOKEN = os.getenv("BOT_TOKEN", "test_bot_token")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789")) # ID for notifications

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/parsergifts")

# Session string instead of file
SESSION_STRING = os.getenv("SESSION_STRING", "")

# Limits and triggers
MARKET_POLL_INTERVAL_SEC = 10 # Frequency of checking market API
TARGET_GIFT_IDS = [
    # IDs of gifts to monitor on the internal market.
    # To find these, you might need to sniff them or look up public lists.
    # E.g., 1001 for some generic gift. The user can fill this in.
    5999277561060787166,
    5898012527257715797,
    6014591077976114307,
    5832644211639321671,
    5886756255493523118
]
LOTS_COUNT_TRIGGER = 3 # Triggers if LOTS_COUNT_TRIGGER lots...
LOTS_TIME_WINDOW_MINUTES = 60 # ...are placed within LOTS_TIME_WINDOW_MINUTES
MIN_GIFTS_TRIGGER = 50 # Or if user has more than MIN_GIFTS_TRIGGER gifts
MIN_RATING_TRIGGER = 1 # Trigger if user has this rating or more

# Userbot Settings
USERBOT_DELAY_BETWEEN_REQUESTS = 2 # Delay between checking profiles to avoid fast bans
