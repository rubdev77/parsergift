import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import BOT_TOKEN, ADMIN_ID
from database import db
from state import AppState
from datetime import datetime

logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def check_user_access(user_id: int) -> bool:
    if user_id == ADMIN_ID:
        return True
    
    active_users = await db.get_active_users()
    return user_id in active_users

async def build_gifts_keyboard():
    # Fetch all global gifts from Telegram via userbot
    if AppState.session_manager:
        all_gifts = await AppState.session_manager.get_all_star_gifts()
    else:
        all_gifts = []
        
    # Get currently enabled gifts from our database
    enabled_gifts = await db.get_target_gifts()
    enabled_set = set(enabled_gifts)
    
    builder = InlineKeyboardBuilder()
    
    # Add control buttons FIRST
    status_text = "🟢 Парсер РАБОТАЕТ" if AppState.is_running else "🔴 Парсер ОСТАНОВЛЕН"
    builder.row(InlineKeyboardButton(text=status_text, callback_data="ignore"))
    
    if AppState.is_running:
        builder.row(InlineKeyboardButton(text="⏸ Остановить Парсинг", callback_data="stop_parsing"))
    else:
        builder.row(InlineKeyboardButton(text="▶️ Начать Парсинг", callback_data="start_parsing"))
    
    # Then add toggle button for each gift
    for gift in all_gifts:
        is_enabled = gift["id"] in enabled_set
        mark = "✅ " if is_enabled else ""
        btn_text = f"{mark}{gift['title']}"
        builder.row(InlineKeyboardButton(
            text=btn_text, 
            callback_data=f"toggle_{gift['id']}"
        ))
        
    return builder.as_markup()


@dp.message(Command("menu", "start"))
async def cmd_menu(message: Message):
    if not await check_user_access(message.from_user.id):
        await message.answer("❌ У вас нет доступа к боту в данное время.")
        return
    
    keyboard = await build_gifts_keyboard()
    await message.answer("🛠 **Панель Управления ParserGifts**\nВыберите подарки для парсинга и нажмите Старт:", reply_markup=keyboard, parse_mode="Markdown")

@dp.message(Command("grant"))
async def cmd_grant(message: Message, command: CommandObject):
    if message.from_user.id != ADMIN_ID:
        return
        
    if not command.args:
        await message.answer("Использование: /grant <user_id> <hours>\nПример: /grant 12345 2 (выдать доступ на 2 часа)")
        return
        
    parts = command.args.split()
    if len(parts) != 2:
        await message.answer("Ошибка: нужно 2 аргумента (user_id, hours).")
        return
        
    try:
        user_id = int(parts[0])
        hours = int(parts[1])
        await db.grant_access(user_id, hours)
        await message.answer(f"✅ Доступ выдан пользователю {user_id} на {hours} ч.")
    except ValueError:
        await message.answer("Ошибка: Аргументы должны быть числами.")

@dp.message(Command("revoke"))
async def cmd_revoke(message: Message, command: CommandObject):
    if message.from_user.id != ADMIN_ID:
        return
        
    if not command.args:
        await message.answer("Использование: /revoke <user_id>")
        return
        
    try:
        user_id = int(command.args.split()[0])
        await db.revoke_access(user_id)
        await message.answer(f"✅ Доступ пользователя {user_id} отозван.")
    except ValueError:
        await message.answer("Ошибка: user_id должен быть числом.")

@dp.callback_query(F.data.startswith("toggle_"))
async def cb_toggle_gift(callback: CallbackQuery):
    if not await check_user_access(callback.from_user.id):
        await callback.answer("У вас нет доступа.", show_alert=True)
        return
        
    gift_id = int(callback.data.split("_")[1])
    
    enabled_gifts = set(await db.get_target_gifts())
    if gift_id in enabled_gifts:
        await db.remove_target_gift(gift_id)
    else:
        await db.add_target_gift(gift_id)
        
    keyboard = await build_gifts_keyboard()
    await callback.message.edit_reply_markup(reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(F.data == "start_parsing")
async def cb_start_parsing(callback: CallbackQuery):
    if not await check_user_access(callback.from_user.id):
        await callback.answer("У вас нет доступа.", show_alert=True)
        return
        
    AppState.is_running = True
    keyboard = await build_gifts_keyboard()
    await callback.message.edit_reply_markup(reply_markup=keyboard)
    await callback.answer("✅ Парсинг запущен!")

@dp.callback_query(F.data == "stop_parsing")
async def cb_stop_parsing(callback: CallbackQuery):
    if not await check_user_access(callback.from_user.id):
        await callback.answer("У вас нет доступа.", show_alert=True)
        return
        
    AppState.is_running = False
    keyboard = await build_gifts_keyboard()
    await callback.message.edit_reply_markup(reply_markup=keyboard)
    await callback.answer("⏸ Парсинг остановлен!")

@dp.callback_query(F.data == "ignore")
async def cb_ignore(callback: CallbackQuery):
    await callback.answer()

async def send_alert(message: str):
    """Sends an alert message to the admin and any active allowed users."""
    if BOT_TOKEN == "test_bot_token":
        logger.info(f"[Mock Alert] To Admin {ADMIN_ID}: {message}")
        return
        
    receivers = await db.get_active_users()
    
    # Если есть пользователи с выданным доступом на этот час - отправляем только им.
    # Если список пуст (никто не арендует бота) - отправляем админу.
    if not receivers:
        receivers = [ADMIN_ID]
        
    for user_id in receivers:
        try:
            await bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            logger.error(f"Failed to send alert to {user_id}: {e}")
            
    logger.info(f"Alert sent to {len(receivers)} users.")

async def close_bot():
    """Closes the bot session during graceful shutdown."""
    await bot.session.close()
