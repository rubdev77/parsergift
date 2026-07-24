import os
from dotenv import load_dotenv

# Загружаем ключи из .env
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if not API_ID or not API_HASH or API_ID == "123456":
    print("Ошибка: Пожалуйста, сначала укажите свои настоящие API_ID и API_HASH в файле .env!")
    exit(1)

# Убедимся, что папка для сессий существует (для временного хранения, пока генерируем строку)
SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)
import hydrogram
from hydrogram import Client as HydroClient

import asyncio

async def main():
    print("=== Утилита для создания сессии ===")
    session_name = input("Введите имя для новой сессии (например, account_1): ").strip()
    
    if not session_name:
        print("Имя сессии не может быть пустым!")
        return

    # Создаем клиента.
    # Так как в проекте используется hydrogram, используем его для генерации
    client = HydroClient(
        name=session_name,
        api_id=int(API_ID),
        api_hash=API_HASH,
        workdir=SESSIONS_DIR
    )

    print("\nЗапуск авторизации... Следуйте инструкциям в консоли.")
    print("Вам потребуется ввести номер телефона, а затем код подтверждения из Telegram.\n")
    
    try:
        # Авторизация в интерактивном режиме
        await client.start()
        
        me = await client.get_me()
        session_string = await client.export_session_string()
        
        print(f"\nУспешно! Сессия для аккаунта {me.first_name} (ID: {me.id}) создана.")
        print("\nВАШ SESSION STRING (скопируйте его целиком):")
        print("-" * 50)
        print(session_string)
        print("-" * 50)
        print("\nВставьте эту строку в ваш файл .env как SESSION_STRING=...")
        
        await client.stop()
    except Exception as e:
        print(f"\nПроизошла ошибка при создании сессии: {e}")

if __name__ == "__main__":
    asyncio.run(main())
