import random
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from ..database.db import db
from ..keyboards.keyboards import get_mining_keyboard

async def cmd_mine(message: types.Message):
    """Обработчик команды шахты"""
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return
        
    keyboard = get_mining_keyboard()
    await message.reply(
        "<b>⛰ Добро пожаловать в шахту!</b>\n<blockquote>Нажмите на кнопку, чтобы начать добычу.</blockquote>",
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )

async def mine_callback(callback_query: types.CallbackQuery):
    """Обработчик кнопки добычи"""
    user_id = callback_query.from_user.id
    stones_found = random.randint(1, 5)
    
    current_stones = db.get_user_stones(user_id)
    db.update_stones(user_id, stones_found)
    
    keyboard = get_mining_keyboard()
    await callback_query.message.edit_text(
        f"<b>⛰ Шахта</b>\n<blockquote>🎉 Вы нашли {stones_found} камней!</blockquote>",
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )

async def cmd_process(message: types.Message):
    """Обработчик команды переработки"""
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return
        
    user_id = message.from_user.id
    stones = db.get_user_stones(user_id)
    
    if not stones:
        await message.reply("<blockquote>У вас нет камней для переработки!</blockquote>", parse_mode=ParseMode.HTML)
        return
    
    coins = stones * 2  # Каждый камень даёт 2 монеты
    
    # Обнуляем камни
    db.update_stones(user_id, -stones)
    # Добавляем монеты
    db.update_balance(user_id, coins)
    
    await message.reply(
        f"<blockquote>Вы переработали {stones} камней и получили {coins} yun-coin!</blockquote>",
        parse_mode=ParseMode.HTML
    )

async def cmd_backpack(message: types.Message):
    """Обработчик команды просмотра сумки"""
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return
        
    user_id = message.from_user.id
    stones = db.get_user_stones(user_id)
    
    await message.reply(f"<blockquote>В вашей сумке {stones} камней</blockquote>", parse_mode=ParseMode.HTML)

def register_handlers(dp):
    """Регистрация обработчиков шахты"""
    dp.register_message_handler(cmd_mine, Text(equals=['зайти в шахту', 'шахта', '/шахта', '!шахта']))
    dp.register_callback_query_handler(mine_callback, lambda c: c.data == "mine_stones")
    dp.register_message_handler(cmd_process, Text(equals=['переработать', '/переработать', '!переработать']))
    dp.register_message_handler(cmd_backpack, Text(equals=['сумка', '/сумка', '!сумка'])) 