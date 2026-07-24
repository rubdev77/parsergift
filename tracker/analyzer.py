import logging
from database import db
from userbot.manager import SessionManager
from parser.sniffer import fetch_latest_market_items
from notifier.bot import send_alert
from config import LOTS_COUNT_TRIGGER, LOTS_TIME_WINDOW_MINUTES, MIN_GIFTS_TRIGGER, MIN_RATING_TRIGGER
from state import AppState

logger = logging.getLogger(__name__)

class MarketTracker:
    def __init__(self, session_manager: SessionManager):
        self.session_manager = session_manager
        # In-memory cache to avoid spamming alerts for the same user repeatedly
        self.alerted_users = set()

    async def process_new_items(self):
        try:
            items = await fetch_latest_market_items(self.session_manager)
            if not items:
                return
            
            for item in items:
                # If admin requested to stop parsing, abort processing the rest of items
                if not AppState.is_running:
                    logger.info("Parsing stopped by admin. Aborting current item list processing.")
                    break
                    
                user_id = item['seller_id']
                username = item.get('username', f'id{user_id}')
                item_name = item['item_name']
                
                # 1. Add to database
                await db.add_market_item(user_id, username, item_name)
                
                # OPTIMIZATION: If we already alerted about this user, skip fetching metrics!
                if user_id in self.alerted_users:
                    continue
                
                user_data = await db.get_user(user_id)
                
                metrics = await self.session_manager.get_user_metrics(user_id)
                if metrics.get("failed"):
                    # We hit a FloodWait or could not fetch metrics. Do NOT alert!
                    continue
                    
                total_gifts = metrics["total_gifts"]
                rating_level = metrics["rating_level"]
                requires_stars = metrics["requires_stars"]
                has_foreign_chars = metrics.get("has_foreign_chars", False)
                
                if total_gifts > 0 or rating_level > 0:
                    await db.update_user_metrics(user_id, total_gifts, rating_level)

                # Apply Filters:
                # 1. Rating must be <= 1
                # 2. Total NFT gifts must be <= 5
                # 3. Requires stars to message must be False
                # 4. No Arabic/CJK characters in profile
                
                is_good_account = (
                    (rating_level <= 1) and 
                    (total_gifts <= 5) and 
                    (not requires_stars) and
                    (not has_foreign_chars)
                )
                
                # If it passes the filter and we haven't alerted yet
                if is_good_account and user_id not in self.alerted_users:
                    msg = (
                        f"🎯 Найден подходящий аккаунт!\n"
                        f"👤 @{username}\n"
                        f"🎁 Лот: {item_name}\n\n"
                        f"✅ Рейтинг (уровень): {rating_level}\n"
                        f"✅ Количество NFT подарков: {total_gifts}\n"
                        f"✅ Написать сообщение: {'Платно ⭐️' if requires_stars else 'Бесплатно'}"
                    )
                    
                    self.alerted_users.add(user_id)
                    await send_alert(msg)
                    logger.info(f"Triggered alert for {username}")
            
        except Exception as e:
            logger.error(f"Error processing market items: {e}", exc_info=True)
