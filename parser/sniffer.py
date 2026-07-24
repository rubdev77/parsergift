import asyncio
import logging
from database import db
from hydrogram.raw.functions.payments import GetResaleStarGifts

logger = logging.getLogger(__name__)

async def _fetch_single_gift_market(gift_id, session_manager):
    items = []
    try:
        try:
            client = await session_manager._get_next_client()
        except ValueError:
            logger.warning("No available clients to fetch market items.")
            return []
            
        resp = await client.invoke(GetResaleStarGifts(
            gift_id=gift_id,
            offset="",
            limit=20 # Get top 20 latest
        ))
        
        users_list = getattr(resp, 'users', [])
        users_dict = {user.id: user for user in users_list}
        
        peers_to_save = []
        for user in users_list:
            peers_to_save.append((
                user.id, 
                getattr(user, 'access_hash', 0), 
                "user", 
                getattr(user, 'username', None), 
                getattr(user, 'phone', None)
            ))
        if peers_to_save:
            await client.storage.update_peers(peers_to_save)
        
        gifts_list = getattr(resp, 'gifts', [])
        
        for gift in gifts_list:
            seller_peer = getattr(gift, 'owner_id', None)
            if seller_peer:
                seller_id = getattr(seller_peer, 'user_id', None)
                if seller_id:
                    username = f"id{seller_id}"
                    if seller_id in users_dict:
                        u = users_dict[seller_id]
                        if getattr(u, 'username', None):
                            username = u.username
                        elif getattr(u, 'first_name', None):
                            username = u.first_name
                            
                    items.append({
                        "seller_id": seller_id,
                        "username": username,
                        "item_name": getattr(gift, 'title', f"Gift {gift_id}")
                    })
    except Exception as e:
        logger.error(f"Error fetching market for gift_id {gift_id}: {e}")
        
    return items

async def fetch_latest_market_items(session_manager):
    """
    Fetches newly listed gifts from the Telegram Star Gifts market 
    using the active userbot sessions concurrently.
    """
    target_gifts = await db.get_target_gifts()
    if not target_gifts:
        logger.warning("No TARGET_GIFT_IDS in database! Cannot poll market.")
        return []

    items = []
    for g_id in target_gifts:
        res = await _fetch_single_gift_market(g_id, session_manager)
        if isinstance(res, list):
            items.extend(res)
        # Small delay to prevent GetResaleStarGifts FloodWaits
        await asyncio.sleep(0.4)
            
    return items
