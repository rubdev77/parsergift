import asyncio
import os
import glob
import time
import logging
from hydrogram import Client
from hydrogram.errors import FloodWait, RPCError
import hydrogram.raw.functions

from config import API_ID, API_HASH

SESSIONS_DIR = "sessions"

logger = logging.getLogger(__name__)

class SessionManager:
    def __init__(self):
        # Store as dict {client: ready_timestamp}
        self.clients = {}
        self.lock = asyncio.Lock()
        
    async def load_sessions(self):
        from config import SESSION_STRING
        if SESSION_STRING:
            logger.info("Loading session from SESSION_STRING environment variable.")
            client = Client(
                name="render_session",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=SESSION_STRING
            )
            self.clients[client] = 0.0
            logger.info("Loaded 1 session from string.")
            return

        # Fallback to local files
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        session_files = glob.glob(os.path.join(SESSIONS_DIR, "*.session"))
        
        if not session_files:
            logger.warning(f"No .session files found in {SESSIONS_DIR} and no SESSION_STRING provided. Please add them.")
            return

        for session_file in session_files:
            session_name = os.path.basename(session_file).replace(".session", "")
            client = Client(
                name=session_name,
                api_id=API_ID,
                api_hash=API_HASH,
                workdir=SESSIONS_DIR,
            )
            self.clients[client] = 0.0 # 0 means ready now
            
        logger.info(f"Loaded {len(self.clients)} sessions.")
        
    async def start_all(self):
        for client in self.clients.keys():
            try:
                await client.start()
                logger.info(f"Started session: {client.name}")
            except Exception as e:
                logger.error(f"Failed to start session {client.name}: {e}")

    async def stop_all(self):
        for client in self.clients.keys():
            if client.is_connected:
                await client.stop()
                logger.info(f"Stopped session: {client.name}")
                
    async def _get_next_client(self) -> Client:
        async with self.lock:
            if not self.clients:
                raise ValueError("No active sessions available.")
            
            now = time.time()
            ready_clients = [c for c, ready_at in self.clients.items() if now >= ready_at]
            
            if not ready_clients:
                # All clients are sleeping due to FloodWait
                soonest_client, ready_time = min(self.clients.items(), key=lambda x: x[1])
                wait_time = ready_time - now
                logger.warning(f"All sessions sleeping. Waiting {wait_time:.2f}s for {soonest_client.name}")
                await asyncio.sleep(wait_time)
                client = soonest_client
            else:
                client = ready_clients[0]
            
            # Rotate: move chosen client to the end of the dict to ensure round-robin
            ready_at = self.clients.pop(client)
            self.clients[client] = ready_at
            
            return client

    async def mark_flood_wait(self, client: Client, wait_seconds: int):
        async with self.lock:
            self.clients[client] = time.time() + wait_seconds

    async def get_user_metrics(self, user_identifier: int | str):
        """Returns dict with metrics. Retries with different clients if FloodWait."""
        if not self.clients:
            logger.warning("No clients loaded, returning mock metrics.")
            return {"failed": True, "total_gifts": 0, "rating_level": 0, "requires_stars": False, "has_foreign_chars": False}
            
        retries = len(self.clients)
        
        for _ in range(max(1, retries)):
            try:
                client = await self._get_next_client()
            except ValueError:
                return {"failed": True, "total_gifts": 0, "rating_level": 0, "requires_stars": False, "has_foreign_chars": False}
                
            try:
                # Fetch full user to get metrics
                # For hydrogram, getting gifts requires raw API invocation
                try:
                    peer = await client.resolve_peer(user_identifier)
                except RPCError as e:
                    if "PEER_ID_INVALID" in str(e) or "USERNAME_NOT_OCCUPIED" in str(e) or "USER_ID_INVALID" in str(e):
                        logger.warning(f"Cannot resolve {user_identifier}. Using mock data for testing.")
                        import random
                        return {"total_gifts": random.randint(0, 100), "rating_level": random.randint(1, 10), "requires_stars": False, "has_foreign_chars": False}
                    raise e

                # Fetch user profile the standard way
                full_user = await client.invoke(hydrogram.raw.functions.users.GetFullUser(id=peer))
                
                # Check message cost
                send_paid_stars = getattr(full_user.full_user, 'send_paid_messages_stars', 0)
                requires_stars = bool(send_paid_stars and send_paid_stars > 0)
                
                # Check rating level
                rating_obj = getattr(full_user.full_user, 'stars_rating', None)
                rating_level = getattr(rating_obj, 'level', 0) if rating_obj else 0
                
                total_gifts = getattr(full_user.full_user, 'gifts_count', 0)

                # Try fetching the Collectibles tab (Star Gifts) using modern raw methods
                # If your library is new enough, it will have GetSavedStarGifts
                try:
                    from hydrogram.raw.functions.payments import GetSavedStarGifts
                    collectibles_resp = await client.invoke(GetSavedStarGifts(
                        peer=peer,
                        limit=100,
                        offset=""
                    ))
                    
                    # Parse the Collectibles
                    # This object contains a list of gifts (models, background, rarity, etc.)
                    gifts_list = getattr(collectibles_resp, 'gifts', [])
                    total_gifts = len(gifts_list)
                    
                    # You can loop through gifts_list here to check backgrounds!
                    # For now we use the total_gifts and rating fallback
                    
                except ImportError:
                    logger.debug("Your library is too old to parse Collectibles directly. Using fallback.")
                except Exception as e:
                    logger.warning(f"Failed to fetch Collectibles tab for {user_identifier}: {e}")
                
                # Check for foreign chars (Arabic, CJK)
                bio = getattr(full_user.full_user, 'about', "") or ""
                first_name = ""
                last_name = ""
                users_list = getattr(full_user, 'users', [])
                if users_list:
                    first_name = getattr(users_list[0], 'first_name', "") or ""
                    last_name = getattr(users_list[0], 'last_name', "") or ""
                
                # Combine all profile text to check
                profile_text = f"{bio} {first_name} {last_name}"
                import re
                # Arabic: \u0600-\u06FF, \u0750-\u077F, \u08A0-\u08FF, \uFB50-\uFDFF, \uFE70-\uFEFF
                # CJK: \u4e00-\u9fff, \u3400-\u4dbf
                foreign_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF\u4E00-\u9FFF\u3400-\u4DBF]')
                has_foreign_chars = bool(foreign_pattern.search(profile_text))

                # Sleep to prevent FloodWait from frequent profile checks
                import asyncio
                await asyncio.sleep(1.0)

                return {
                    "total_gifts": total_gifts,
                    "rating_level": rating_level,
                    "requires_stars": requires_stars,
                    "has_foreign_chars": has_foreign_chars
                }

            except FloodWait as e:
                logger.warning(f"Session {client.name} got FloodWait for {e.value} seconds.")
                await self.mark_flood_wait(client, e.value)
                continue # Try next client
            except RPCError as e:
                logger.error(f"RPC Error on {client.name} for user {user_identifier}: {e}")
                break # Non-recoverable error for this user
            except Exception as e:
                logger.error(f"Unknown error getting metrics for {user_identifier}: {e}")
                break
                
        return {"failed": True, "total_gifts": 0, "rating_level": 0, "requires_stars": False, "has_foreign_chars": False}

    async def get_all_star_gifts(self):
        """Fetches the global list of all Star Gifts from Telegram."""
        if not self.clients:
            return []
            
        try:
            client = await self._get_next_client()
        except ValueError:
            return []
            
        try:
            from hydrogram.raw.functions.payments import GetStarGifts
            resp = await client.invoke(GetStarGifts(hash=0))
            gifts = getattr(resp, 'gifts', [])
            
            result = []
            for g in gifts:
                title = getattr(g, 'title', None)
                if not title:
                    # Ignore regular non-NFT gifts (they don't have titles)
                    continue
                    
                result.append({
                    "id": getattr(g, 'id', 0),
                    "title": title
                })
            return result
        except Exception as e:
            logger.error(f"Error fetching global star gifts: {e}")
            return []
