from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode

from NIVEAbot.database.db import db
from ..utils.helpers import check_permissions, format_time, get_current_timestamp
from ..config.config import BONUS_COOLDOWN, WORK_COOLDOWN

async def check_cooldown(user_id: int, command: str, cooldown: int) -> tuple[bool, int]:
    """Проверка времени ожидания команды"""
    current_ts = get_current_timestamp()
    
    db.cursor.execute(
        'SELECT last_action_ts FROM last_actions WHERE user_id = ? AND command_name = ?', 
        (user_id, command)
    )
    last_action = db.cursor.fetchone()
    
    if last_action:
        time_since_last = current_ts - last_action[0]
        if time_since_last < cooldown:
            return False, cooldown - time_since_last
    return True, 0

async def cmd_bonus(message: types.Message):
    """Обработчик команды бонус"""
    user_id = message.from_user.id
    
    can_collect, wait_time = await check_cooldown(user_id, 'бонус', BONUS_COOLDOWN)
    if not can_collect:
        await message.reply(
            f"Вы уже забрали бонус недавно. "
            f"<blockquote>Следующий бонус через {format_time(wait_time)}</blockquote>",
            parse_mode=ParseMode.HTML
        )
        return
    
    bonus_amount = random.randint(600, 2200)
    db.update_balance(user_id, bonus_amount)
    
    # Обновляем время последнего действия
    db.cursor.execute(
        'REPLACE INTO last_actions (user_id, command_name, last_action_ts) VALUES (?, ?, ?)',
        (user_id, 'бонус', get_current_timestamp())
    )
    db.conn.commit()
    
    await message.reply(
        f"Бонус в виде <code>{bonus_amount}</code> <b>yun-coin</b>",
        parse_mode=ParseMode.HTML
    )

async def cmd_work(message: types.Message):
    """Обработчик команды ворк"""
    user_id = message.from_user.id
    
    can_work, wait_time = await check_cooldown(user_id, 'ворк', WORK_COOLDOWN)
    if not can_work:
        await message.reply(
            f"Вы уже были на работе недавно. "
            f"<blockquote>Следующая работа через {format_time(wait_time)}</blockquote>",
            parse_mode=ParseMode.HTML
        )
        return
    
    work_amount = random.randint(350, 1250)
    db.update_balance(user_id, work_amount)
    
    # Обновляем время последнего действия
    db.cursor.execute(
        'REPLACE INTO last_actions (user_id, command_name, last_action_ts) VALUES (?, ?, ?)',
        (user_id, 'ворк', get_current_timestamp())
    )
    db.conn.commit()
    
    await message.reply(
        f"Вы поработали на подработке, и получили <code>{work_amount}</code> <b>yun-coin</b>",
        parse_mode=ParseMode.HTML
    )

async def cmd_balance(message: types.Message):
    """Обработчик команды баланс"""
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    user_link = f'<a href="tg://user?id={user_id}">{username}</a>'
    
    # Получаем или создаем запись пользователя
    db.cursor.execute('SELECT * FROM honey WHERE user_id = ?', (user_id,))
    record = db.cursor.fetchone()
    
    if not record:
        db.cursor.execute(
            'INSERT INTO honey (user_id, username, user_link) VALUES (?, ?, ?)',
            (user_id, username, user_link)
        )
        db.conn.commit()
        honey_count = 0
        theme = 'стандарт'
    else:
        honey_count = record[1]
        theme = record[5]
    
    if theme == 'стандарт':
        text = f"<u>Кошелек</u> {user_link}\n<blockquote>обычный счет - <code>{honey_count}</code> <b>yun-coin</b></blockquote>"
    else:
        text = f"Кошелек {user_link},\nваш счет - <code>{honey_count}</code> yun-coin 🪙"
    
    await message.reply(text, parse_mode=ParseMode.HTML)

async def cmd_give(message: types.Message):
    """Обработчик команды отдать"""
    user_id = message.from_user.id
    reply_msg = message.reply_to_message
    
    if not reply_msg or reply_msg.from_user.id == user_id:
        await message.reply("<b>Вы не выбрали пользователя для передачи.</b>", parse_mode=ParseMode.HTML)
        return
    
    try:
        amount = int(message.text.split()[1])
        if amount < 0:
            await message.reply("Вы не можете отправить отрицательную сумму.")
            return
            
        sender_balance = db.get_user_balance(user_id)
        if sender_balance < amount:
            await message.reply("У вас недостаточное количество средств на балансе.")
            return
        
        # Выполняем передачу
        db.update_balance(user_id, -amount)
        db.update_balance(reply_msg.from_user.id, amount)
        
        await message.reply(
            f"{amount} yun-coin были отправлены на кошелек - {reply_msg.from_user.username}.\n"
            f"<blockquote>Счет вашего кошелька: {sender_balance - amount}</blockquote>",
            parse_mode=ParseMode.HTML
        )
        
    except (IndexError, ValueError):
        await message.reply(
            "Некорректный формат команды. <blockquote>Используйте: 'отдать <число>'.</blockquote>",
            parse_mode=ParseMode.HTML
        )

def register_handlers(dp):
    """Регистрация обработчиков экономики"""
    dp.register_message_handler(cmd_bonus, Text(equals=['бонус']))
    dp.register_message_handler(cmd_work, Text(equals=['ворк']))
    dp.register_message_handler(cmd_balance, Text(equals=['Кошелек', 'кошелек', 'кошелёк', 'Кошелёк', 'я', 'Я']))
    dp.register_message_handler(cmd_give, Text(startswith=['отдать'])) 