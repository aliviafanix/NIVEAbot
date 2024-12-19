import random
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ParseMode

from ..database.db import db
from ..utils.helpers import parse_amount

async def cmd_rps(message: types.Message):
    """Обработчик игры камень-ножницы-бумага"""
    if message.chat.type == 'private':
        await message.reply("<b>Эта команда доступна только в группах!</b>", parse_mode=ParseMode.HTML)
        return
    
    try:
        args = message.text.split()
        if len(args) < 2:
            await message.reply(
                "Неверная команда. <blockquote>Используйте: /кнб [камень/ножницы/бумага] [ставка] или /кнб [выбор] вб</blockquote>",
                parse_mode=ParseMode.HTML
            )
            return
            
        choice = args[1].lower()
        if choice not in ["камень", "ножницы", "бумага"]:
            await message.reply("<b>Неверный выбор.</b>", parse_mode=ParseMode.HTML)
            return
        
        user_balance = db.get_user_balance(message.from_user.id)
        if not user_balance:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
            return
            
        bet = parse_amount(args[2] if len(args) > 2 else str(user_balance), user_balance)
        if bet is None:
            await message.reply("<b>Неверный формат ставки.</b>", parse_mode=ParseMode.HTML)
            return
            
        bot_choice = random.choice(["камень", "ножницы", "бумага"])
        
        if choice == bot_choice:
            result = "Ничья"
            win_amount = 0
        elif (choice == "камень" and bot_choice == "ножницы") or \
             (choice == "ножницы" and bot_choice == "бумага") or \
             (choice == "бумага" and bot_choice == "камень"):
            result = "Вы выиграли"
            win_amount = bet
        else:
            result = "Вы проиграли"
            win_amount = -bet
            
        if win_amount != 0:
            db.update_balance(message.from_user.id, win_amount)
            
        text = f"<blockquote>Вы выбрали: {choice}\nБот выбрал: {bot_choice}</blockquote> "
        if win_amount > 0:
            text += f"<u>{result}</u>: +<code>{win_amount}</code> <b>yun-coin</b>"
        elif win_amount < 0:
            text += f"<u>{result}</u>: -<code>{abs(win_amount)}</code> <b>yun-coin</b>"
        else:
            text += f"<u>{result}</u>"
            
        await message.reply(text, parse_mode=ParseMode.HTML)
        
    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)

async def cmd_roulette(message: types.Message):
    """Обработчик игры рулетка"""
    try:
        user_balance = db.get_user_balance(message.from_user.id)
        if not user_balance:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
            return
            
        bet = parse_amount(message.text.split()[1], user_balance)
        if bet is None:
            await message.reply("<b>Неверный формат ставки.</b>", parse_mode=ParseMode.HTML)
            return
            
        roll = random.randint(1, 10)
        
        if roll <= 5:  # 50% на проигрыш
            win_amount = -bet
            text = f"<blockquote>Барабан крутился и... <b>БАБАХ!</b></blockquote>"
        elif roll <= 8:  # 30% на выигрыш x1.5
            win_amount = int(bet * 0.5)
            text = f"<blockquote>Барабан крутился и... <b>КЛИК!</b></blockquote>"
        else:  # 20% на выигрыш x2
            win_amount = bet
            text = f"<blockquote>Барабан крутился и... <b>КЛИК!</b></blockquote>"
            
        db.update_balance(message.from_user.id, win_amount)
        
        if win_amount > 0:
            text += f" <u>Вы выиграли</u>: +<code>{win_amount}</code> <b>yun-coin</b>"
        else:
            text += f" <u>Вы проиграли</u>: -<code>{abs(win_amount)}</code> <b>yun-coin</b>"
            
        await message.reply(text, parse_mode=ParseMode.HTML)
        
    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)

async def cmd_elite(message: types.Message):
    """Обработчик элитного казино"""
    try:
        user_balance = db.get_user_balance(message.from_user.id)
        if not user_balance:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
            return
            
        bet = parse_amount(message.text.split()[1], user_balance)
        if bet is None or bet < 10000:
            await message.reply("<b>Минимальная ставка в элитном казино составляет 10000 yun-coin.</b>", parse_mode=ParseMode.HTML)
            return
            
        roll = random.randint(1, 100)
        
        if roll <= 90:  # 90% на проигрыш
            multiplier = 0
        elif roll <= 97:  # 7% на x3
            multiplier = 3
        elif roll <= 99:  # 2% на x4.5
            multiplier = 4.5
        else:  # 1% на x5
            multiplier = 5
            
        win_amount = int(bet * multiplier) - bet
        db.update_balance(message.from_user.id, win_amount)
        
        if win_amount > 0:
            text = f"<blockquote><b>Вы выиграли!</b></blockquote> <u>Выигрыш</u>: +<code>{win_amount}</code> <b>yun-coin</b>"
        else:
            text = f"<blockquote><b>Вы проиграли</b></blockquote> <u>Теряете</u>: -<code>{abs(win_amount)}</code> <b>yun-coin</b>"
            
        await message.reply(text, parse_mode=ParseMode.HTML)
        
    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)

async def cmd_casino(message: types.Message):
    """Обработчик обычного казино"""
    try:
        user_balance = db.get_user_balance(message.from_user.id)
        if not user_balance:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
            return
            
        bet = parse_amount(message.text.split()[1], user_balance)
        if bet is None:
            await message.reply("<b>Неверный формат ставки.</b>", parse_mode=ParseMode.HTML)
            return
            
        is_win = random.choice([True, False])
        win_amount = bet if is_win else -bet
        
        db.update_balance(message.from_user.id, win_amount)
        
        if win_amount > 0:
            text = f"<blockquote><b>Вы выиграли!</b></blockquote> <u>Получаете</u>: +<code>{win_amount}</code> <b>yun-coin</b>"
        else:
            text = f"<blockquote><b>Вы проиграли.</b></blockquote> <u>Теряете</u>: -<code>{abs(win_amount)}</code> <b>yun-coin</b>"
            
        await message.reply(text, parse_mode=ParseMode.HTML)
        
    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)

def register_handlers(dp):
    """Регистрация игровых обработчиков"""
    dp.register_message_handler(cmd_rps, Command(['кнб', 'Кнб'], prefixes='!./'))
    dp.register_message_handler(cmd_roulette, Command(['рулетка', 'Рулетка'], prefixes='!./'))
    dp.register_message_handler(cmd_elite, Command(['элит', 'Элит'], prefixes='!./'))
    dp.register_message_handler(cmd_casino, Command(['казино', 'Казино'], prefixes='!./')) 