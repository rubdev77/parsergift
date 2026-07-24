import asyncio
import logging
import signal
import sys
from config import MARKET_POLL_INTERVAL_SEC
from database import db
from userbot.manager import SessionManager
from tracker.analyzer import MarketTracker
from notifier.bot import close_bot
from state import AppState

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("hydrogram.session.session").setLevel(logging.ERROR)
logging.getLogger("hydrogram").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting ParserGifts...")
    
    # Initialize DB (which also copies TARGET_GIFT_IDS if empty)
    await db.init_db()
    
    session_manager = SessionManager()
    await session_manager.load_sessions()
    
    AppState.session_manager = session_manager
    
    # Start all Pyrogram clients (userbots)
    await session_manager.start_all()
    
    # Start bot polling in the background
    from notifier.bot import dp, bot
    bot_task = asyncio.create_task(dp.start_polling(bot))
    
    tracker = MarketTracker(session_manager)
    
    # Loop task
    loop_task = None
    
    try:
        while True:
            if AppState.is_running:
                logger.info("Polling market items...")
                await tracker.process_new_items()
                await asyncio.sleep(MARKET_POLL_INTERVAL_SEC)
            else:
                await asyncio.sleep(2) # Sleep while idle
            
    except asyncio.CancelledError:
        logger.info("Main loop cancelled.")
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received.")
    finally:
        # Graceful shutdown sequence
        logger.info("Shutting down gracefully...")
        if loop_task and not loop_task.done():
            loop_task.cancel()
            
        await session_manager.stop_all()
        await close_bot()
        logger.info("Shutdown complete.")

if __name__ == "__main__":
    # Workaround for ProactorEventLoop and KeyboardInterrupt on Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
