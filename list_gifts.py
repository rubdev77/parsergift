import asyncio
import logging
from hydrogram import Client
from hydrogram.raw.functions.payments import GetStarGifts
from config import API_ID, API_HASH

async def main():
    print("Убедитесь, что в папке sessions/ есть хотя бы одна сессия.")
    client = Client("sessions/1", api_id=API_ID, api_hash=API_HASH, workdir=".")
    await client.start()
    
    print("Получаем список всех существующих подарков...")
    resp = await client.invoke(GetStarGifts(hash=0))
    
    gifts_list = getattr(resp, 'gifts', [])
    for gift in gifts_list:
        gift_id = getattr(gift, 'id', None)
        title = getattr(gift, 'title', 'Unknown')
        print(f"Подарок: {title} | ID: {gift_id}")
        
    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
