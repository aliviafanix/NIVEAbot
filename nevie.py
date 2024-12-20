import logging
import asyncio
import time
import sqlite3
from datetime import datetime, timedelta
import PIL
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

import psutil
import re
import random
import os
import traceback
import io
import sys
import string 
import html
import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.callback_data import CallbackData
import sqlite3
import random
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint
import time
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import MessageToEditNotFound
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold, hcode
from random import randint
import asyncio
import os
import random
from typing import Optional

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import logging
from aiogram import Bot, Dispatcher, types
import g4f
from aiogram.utils import executor


API_TOKEN = "7234887704:AAH3QGIu_uEK8kRs8gEtkHCmUD-5JX8xeeo"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

import asyncio
import time
import random
import platform
from aiogram import Bot, Dispatcher, types

start_time = time.time()


@dp.message_handler(lambda message: message.text.lower() == "пинг")
async def ping_handler(message: types.Message):
    try:
        if platform.system() == "Windows":
            server_name = platform.node()
        elif platform.system() == "Linux":
            server_name = platform.node()
        elif platform.system() == "Darwin":
            server_name = platform.node()
        else:
            server_name = "Неизвестный сервер"

        latency = random.uniform(0.01, 0.5)
        latency_ms = latency * 1000

        uptime_seconds = int(time.time() - start_time)
        uptime_days = uptime_seconds // (24 * 3600)
        uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60
        uptime_seconds = uptime_seconds % 60

        possible_latency = random.randint(1, 5)

        text = f"\U0001F5A5 Сервер: {server_name}\n\u26A1 Задержка: {latency_ms:.2f} мсек\n\u23F0 Время работы: {uptime_days}д, {uptime_hours}ч, {uptime_minutes}м\n\U0001F4CA Возможная задержка: {possible_latency}с"

        await message.answer(text)
    except Exception as e:
        await message.answer(f"\u274C Ошибка: {e}")


async def main():
    await dp.start_polling()

class SaveMessages(StatesGroup):
    saving = State()

raz_ids = [6558424230, 6998521871, 5932424109, 7241965595]
admin_ids = [ 7241965595 ]

conn = sqlite3.connect('honey.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin_users (
        user_id INTEGER PRIMARY KEY
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS honey (
        user_id INTEGER PRIMARY KEY,
        honey_count INTEGER DEFAULT 0,
        last_collection_ts INTEGER,
        username TEXT,
        user_link TEXT,
        theme TEXT DEFAULT 'стандарт'
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        stones INTEGER DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS modules (
        chat_id INTEGER,
        module_name TEXT,
        is_enabled INTEGER DEFAULT 1,
        PRIMARY KEY (chat_id, module_name)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS beta_access (
        chat_id INTEGER PRIMARY KEY,
        enabled INTEGER DEFAULT 0
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_modules (
        module_name TEXT PRIMARY KEY,
        module_type TEXT,
        description TEXT,
        commands TEXT,
        response_type TEXT,
        response_data TEXT
    )
''')

# Создаем таблицу для истории чата
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        user_id INTEGER,
        message TEXT,
        response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

cursor.execute("SELECT user_id FROM admin_users")
admin_ids = [row[0] for row in cursor.fetchall()]

def check_permissions(user_id):
    return user_id in admin_ids or user_id in raz_ids


def update_db():
    while True:
        new_users = get_new_users()
        if new_users:
            for user_id, username in new_users:
                add_user_to_db(user_id, username)
        time.sleep(60)
def get_new_users():
    return [] 




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text="ℹ️ my weekdays", url="https://t.me/rvh_ebator")
    url_button2 = types.InlineKeyboardButton(text="➕", url="https://t.me/nevie_cfbot?startgroup=start")
    keyboard.add(url_button1, url_button2)
    
    quoted_message = f"""
🐙 nevie - игровой проект по <u>тематике развлечение.</u>
<blockquote>ℹ️ просмот меню по слову - <code>меню</code></blockquote>
    """

    await message.reply(quoted_message, reply_markup=keyboard, parse_mode=ParseMode.HTML)






@dp.message_handler(lambda message: message.text.lower() in ["меню"])
async def commands(message: types.Message):

    rate = InlineKeyboardButton("зарабаток", callback_data="rate")
    nick = InlineKeyboardButton("основы", callback_data="nick")
    pref = InlineKeyboardButton("развлечение", callback_data="pref")

    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    floor.row(rate, pref)
    floor.row(nick)


    await message.answer("""<b>выбор:</b>""", parse_mode="HTML", reply_markup=floor)



@dp.callback_query_handler(text=['backtocommlistbtn'])
async def back_to_commands(call: types.CallbackQuery):
    rate = InlineKeyboardButton("зарабаток", callback_data="rate")
    nick = InlineKeyboardButton("основы", callback_data="nick")
    pref = InlineKeyboardButton("развлечение", callback_data="pref")

    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    floor.row(rate, pref)
    floor.row(nick)

    await call.message.edit_text("""<b>выбор:</b>""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['rate'])
async def rate_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("↩️ вернутся", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)

    await call.message.edit_text("""
<b>•</b> <code>бонус</code> <b>&</b> <code>ворк</code>
<blockquote><b>фарм ваших yun-coin, в двух командах присутствует тайм взаимодействи,  3 часа от бонуса, и 20 минут от ворка.</b></blockquote>
<b>•</b> <code>зайти в шахту</code> <b>&</b> <code>переработать</code>
<blockquote><b>зайдите в шахту и начните собирать камни чтобы в дальнейшем их переработать и получить коины. переработка происхолит по курсу один камень - два коина.</b></blockquote>
""", parse_mode="HTML", reply_markup=floor)


@dp.callback_query_handler(text=['nick'])
async def nick_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("↩️ вернутся", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""
<b>•</b> <code>кошелек</code> <b>&</b> <code>сумка</code>
<blockquote><b>просмотр вашего счета и данных на вашем кошельке. так же просмотр сумки предостовяет вам то сколько у вас камней для переработки.</b></blockquote>
<b>•</b> <code>отдать [сумма]</code>
<blockquote><b>отдать пользователю указаную сумму коинов на его кошельковый счет.</b></blockquote>
<b>•</b> <code>тматики стандарт/оформительная</code>
<blockquote><b>меняйте оформление своего кошелька на второстепеное оформление созданое для всех кто не желает видить цитировку.</b></blockquote>
""", parse_mode="HTML", reply_markup=floor)


@dp.callback_query_handler(text=['pref'])
async def pref_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("↩️ вернутся", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""
<b>•</b> <code>/рулетка</code> <i>[сумма ставки]</i>
<blockquote><b>в зависимости от вас, на кону вы и ваша ставка.</b></blockquote>
<b>•</b> <code>/элит</code> <i>[сумма ставки]</i>
<blockquote><b>элитное казино, сыграйте с минимальной ставкой в 10.000 чтобы попытать свою удачу.</b></blockquote>
<b>•</b> <code>/казино</code> <i>[сумма ставки]</i>
<blockquote><b>играете в казино чтобы попытать удачу на победу с большим множителем.</b></blockquote>
<b>•</b> <code>/кнб</code> <i>[камень/ножницы/бумага] [сумма ставки]</i>
<blockquote><b>играйте в камень ножницы бумага с неким искуственым рандомайжером.</b></blockquote>
    """, parse_mode="HTML", reply_markup=floor)






@dp.message_handler(Text(equals=['Кошелек', 'кошелек', 'кошелёк', 'Кошелёк', 'я', 'Я']))
async def my_backpack(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    user_link = f'<a href="tg://user?id={user_id}">{username}</a>'

    cursor.execute('SELECT 1 FROM honey WHERE user_id = ?', (user_id,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute('INSERT INTO honey (user_id, username, user_link) VALUES (?, ?, ?)', (user_id, username, user_link))
        conn.commit()

    cursor.execute('SELECT * FROM honey WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()

    if record:
        honey_count = record[1]
        theme = record[5]
    else:
        honey_count = 0
        theme = 'стандарт'

    if theme == 'стандарт':
        await message.reply(f"<u>Кошелек</u> {user_link}\n<blockquote>обычный счет - <code>{honey_count}</code> <b>yun-coin</b></blockquote>", parse_mode=ParseMode.HTML)
    elif theme == 'оформительная':
        await message.reply(f"Кошелек {user_link},\nваш счет - <code>{honey_count}</code> yun-coin 🪙", parse_mode=ParseMode.HTML)




@dp.message_handler(Text(startswith='тематика '))
async def set_theme(message: types.Message):
    user_id = message.from_user.id
    theme_choice = message.text.split(' ')[1].lower()

    cursor.execute('SELECT theme FROM honey WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()
    current_theme = record[0] if record else 'стандарт'

    if theme_choice == 'стандарт':
        if current_theme == 'стандрт':
            await message.reply('У вас уже установлена стандартная тема.')
        else:
            cursor.execute('UPDATE honey SET theme = ? WHERE user_id = ?', ('стандарт', user_id))
            conn.commit()
            await message.reply('Тема изменена на стандартную.', parse_mode="HTML")
    elif theme_choice == 'обычная':
        if current_theme == 'обычная':
            await message.reply('У вас уже установлена тема "обычная".', parse_mode="HTML")
        else:
            cursor.execute('UPDATE honey SET theme = ? WHERE user_id = ?', ('оформительная', user_id))
            conn.commit()
            await message.reply('Тема изменена на "обычная".', parse_mode="HTML")
    elif theme_choice == 'обычная':
        await message.reply('Кажется, вы имели в виду "обычная". Хотите выбрать эту тему? ', parse_mode="HTML")
    else:
        await message.reply('Неверный вариант темы. Доступны темы: стандарт, оформительная.', parse_mode="HTML")







@dp.message_handler(lambda message: message.text.lower() == 'бонус')
async def gather_honey(message: types.Message):
    if not await check_module(message, 'бонус'):
        return
    user_id = message.from_user.id
    current_ts = int(datetime.datetime.now().timestamp())
    command_name = 'бонус'

    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="last_actions";')
    table_exists = cursor.fetchone() is not None

    if not table_exists:
        cursor.execute('CREATE TABLE last_actions (user_id INTEGER PRIMARY KEY, command_name TEXT, last_action_ts INTEGER);')
        conn.commit()

    cursor.execute('SELECT * FROM last_actions WHERE user_id = ? AND command_name = ?', (user_id, command_name))
    last_action_record = cursor.fetchone()

    if last_action_record:
        last_action_ts = last_action_record[2]
        time_since_last_action = current_ts - last_action_ts
        time_until_next_action = max(0, 3 * 60 * 60 - time_since_last_action)

        if time_since_last_action < 3 * 60 * 60:
            hours = time_until_next_action // 3600
            minutes = (time_until_next_action % 3600) // 60
            seconds = time_until_next_action % 60
            await message.reply(f"Вы уже забрали бонус недавно. <blockquote>Вы сможете собрать ��нов через {hours} часов, {minutes} минут и {seconds} секунд.</blockquote>", parse_mode=ParseMode.HTML)
            return

    honey_to_add = random.randint(600, 2200)
    cursor.execute('SELECT * FROM honey WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()

    if record:
        new_honey_count = record[1] + honey_to_add
        cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (new_honey_count, user_id))
    else:
        cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (user_id, honey_to_add))

    cursor.execute('REPLACE INTO last_actions (user_id, command_name, last_action_ts) VALUES (?, ?, ?)', (user_id, command_name, current_ts))

    conn.commit()

    await message.reply(f"Бонус в виде <code>{honey_to_add}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)






@dp.message_handler(lambda message: message.text.lower() == 'ворк')
async def gather_honey(message: types.Message):
    if not await check_module(message, 'ворк'):
        return
    user_id = message.from_user.id
    current_ts = int(datetime.datetime.now().timestamp())
    command_name = 'ворк'

    cursor.execute('CREATE TABLE IF NOT EXISTS last_actions (user_id INTEGER, command_name TEXT, last_action_ts INTEGER, PRIMARY KEY (user_id, command_name))')

    cursor.execute('SELECT * FROM last_actions WHERE user_id = ? AND command_name = ?', (user_id, command_name))
    last_action_record = cursor.fetchone()

    if last_action_record:
        last_action_ts = last_action_record[2]
        time_since_last_action = current_ts - last_action_ts
        time_until_next_action = max(0, 20 * 60 - time_since_last_action) 

        if time_since_last_action < 20 * 60:
            minutes = (time_until_next_action % 3600) // 60
            seconds = time_until_next_action % 60
            await message.reply(f"Вы уже были на дополнительной роботе. <blockquote>Вы сможете еще поработать через {minutes} минут и {seconds} секунд.</blockquote>", parse_mode=ParseMode.HTML)
            return

    honey_to_add = random.randint(350, 1250)
    cursor.execute('SELECT * FROM honey WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()

    if record:
        new_honey_count = record[1] + honey_to_add
        cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (new_honey_count, user_id))
    else:
        cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (user_id, honey_to_add))

    cursor.execute('REPLACE INTO last_actions (user_id, command_name, last_action_ts) VALUES (?, ?, ?)', (user_id, command_name, current_ts))

    conn.commit()

    await message.reply(f"Вы поработали на подработке, и получили <code>{honey_to_add}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)






@dp.message_handler(lambda message: message.text.lower().startswith('отдать'))
async def give_honey(message: types.Message):
    user_id = message.from_user.id
    response_message = message.reply_to_message

    if response_message and response_message.from_user.id != user_id:
        try:
            if len(message.text.lower().split()) >= 2:
                amount = int(message.text.lower().split()[1]) 
            else:
                await message.reply("Некорректный формат команды. <blockquote>Используйте: 'отдать <число>'.</blockquote>", parse_mode=ParseMode.HTML)
                return

            if amount < 0:
                await message.reply("Вы не можете отправить отрицательную сумму.")
                return

            cursor.execute('SELECT * FROM honey WHERE user_id = ?', (user_id,))
            sender_record = cursor.fetchone()

            if not sender_record:
                cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (user_id, 0))
                conn.commit()
                sender_record = cursor.fetchone()

            if sender_record[1] < amount:
                await message.reply("У вас недостаточное количество средств на балансе.")
                return

            cursor.execute('SELECT * FROM honey WHERE user_id = ?', (response_message.from_user.id,))
            recipient_record = cursor.fetchone()

            if not recipient_record:
                cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (response_message.from_user.id, 0))
                conn.commit()
                recipient_record = cursor.fetchone()

            if sender_record and recipient_record:
                sender_new_balance = sender_record[1] - amount
                recipient_new_balance = recipient_record[1] + amount

                cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (sender_new_balance, user_id))
                cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (recipient_new_balance, response_message.from_user.id))
                conn.commit()

                await message.reply(f"{amount} yun-coin были отправлены на кошелек - {response_message.from_user.username}.\n<blockquote>Счет вашего кошелька: {sender_new_balance}</blockquote>", parse_mode=ParseMode.HTML)
            else:
                await message.reply("У одного из пользователей нет кошелька.")
        except (IndexError, ValueError):
            await message.reply("Некорректный формат команды. <blockquote>Используйте: 'отдать <ч��сло>'.</blockquote>", parse_mode=ParseMode.HTML)
    else:
        await message.reply("<b>Вы не выбрали пользователя для передачи.</b>", parse_mode=ParseMode.HTML)





@dp.message_handler(commands=["кнб", "Кнб"], commands_prefix='!./')
async def bot_rps(message: types.Message):
    if message.chat.type == 'private':
        await message.reply("<b>Эта команда доступна только в группах!</b>", parse_mode=ParseMode.HTML)
        return

    if not await check_module(message, 'кнб'):
        return

    try:
        args = message.text
        user_id = message.from_user.id
        username = message.from_user.username
        if len(args.split()) in [2, 3]:
            command, choice = args.split()[:2] 
            if choice not in ["камень", "ножницы", "бумага"]:
                await message.reply("<b>Неверный выбор.</b>", parse_mode=ParseMode.HTML)
                return

            cursor.execute("SELECT honey_count FROM honey WHERE user_id == ?", (user_id,))
            result = cursor.fetchone()
            if not result:
                await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
                return

            if len(args.split()) == 3: 
                if args.split()[2] == "вб":
                    bet = result[0]  
                elif args.split()[2].isdigit():
                    bet = int(args.split()[2])
                else:
                    await message.reply("<b>Неверный формат ставки.</b>", parse_mode=ParseMode.HTML)
                    return
            else:  
                bet = result[0] 

            if result[0] < bet:
                await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
                return

            user_choice = choice
            bot_choice = random.choice(["камень", "ножницы", "бумага"])

            if user_choice == bot_choice:
                await message.reply(f"<blockquote>Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}</blockquote> <u>Ничья</u>", parse_mode=ParseMode.HTML)
            elif (user_choice == "камень" and bot_choice == "ножницы") or (user_choice == "ножницы" and bot_choice == "бумага") or (user_choice == "бумага" and bot_choice == "камень"):
                cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id == ?",
                               (bet, user_id)) 
                conn.commit()
                await message.reply(f"<blockquote>Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}</blockquote> <u>Вы выиграли</u>: +<code>{bet}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)
            else:
                cursor.execute("UPDATE honey SET honey_count = honey_count - ? WHERE user_id == ?", (bet, user_id)) 
                conn.commit()
                await message.reply(f"<blockquote>Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}</blockquote> <u>Вы проиграли</u>: -<code>{bet}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)

        else:
            await message.reply("Неверная команда. <blockquote>Используйте: /кнб [камень/ножницы/бумага] [ставка] или /кнб [камень/ножницы/бумага] вб</blockquote>", parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)





@dp.message_handler(commands=["рулетка", "Рулетка"], commands_prefix='!./')
async def bot_russian_roulette(message: types.Message):
    if not await check_module(message, 'рулетка'):
        return
    try:
        user_id = message.from_user.id
        username = message.from_user.username
        cursor.execute("SELECT honey_count FROM honey WHERE user_id == ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
        elif result[0] == 0:
            await message.reply("<b>У вас недостаточно yun-coin для игры в рулетку.</b>", parse_mode=ParseMode.HTML)
        else:
            bet = result[0] if message.text.split()[1] == "вб" else int(message.text.split()[1])

            if bet > result[0]:
                await message.reply("<b>У вас недостаточно yun-coin для этой ставки.</b>", parse_mode=ParseMode.HTML)
                return

            roll = random.randint(1, 10)

            if roll <= 5: 
                cursor.execute("UPDATE honey SET honey_count = honey_count - ? WHERE user_id == ?", (bet, user_id))
                conn.commit()
                await message.reply(f"<blockquote>Барабан крутился и... <b>БАБАХ!</b></blockquote> <u>Вы проиграли</u>: -<code>{bet}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)
            elif roll <= 8: 
                multiplier = 1.5
                winnings = round(bet * (multiplier - 1))
                cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id == ?", (winnings, user_id))
                conn.commit()
                await message.reply(f"<blockquote>Барабан крутился и... <b>КЛИК!</b></blockquote> <u>Вы выиграли</u>: +<code>{winnings}</code> <b>yun-coin</b> <b>(x{multiplier:.1f})</b>", parse_mode=ParseMode.HTML)
            else: 
                multiplier = 2
                winnings = round(bet * (multiplier - 1))
                cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id == ?", (winnings, user_id))
                conn.commit()
                await message.reply(f"<blockquote>Барабан крутился и... <b>КЛИК!</b></blockquote> <u>Вы выиграли</u>: +<code>{winnings}</code> <b>yun-coin</b> <b>(x{multiplier:.1f})</b>", parse_mode=ParseMode.HTML)

    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)





@dp.message_handler(commands=["элит", "Элит"], commands_prefix='!./')
async def bot_elite_casino(message: types.Message):
    if not await check_module(message, 'элит'):
        return
    try:
        user_id = message.from_user.id
        username = message.from_user.username
        cursor.execute("SELECT honey_count FROM honey WHERE user_id == ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            await message.reply("<b>У вас недостаточно yun-coin</b>", parse_mode=ParseMode.HTML)
        else:
            bet = message.text.split()[1]
            if not bet.isdigit():
                await message.reply("Ставка должна быть числом.")
                return

            bet = int(bet)

            if bet < 10000:
                await message.reply("<b>Минимальная ставка в элитном казино составляет 10000 yun-coin.</b>", parse_mode=ParseMode.HTML)
                return

            if bet > result[0]: 
                await message.reply("<b>У вас недостаточно yun-coin для этой ставки.</b>", parse_mode=ParseMode.HTML)
                return

            roll = random.randint(1, 100)

            if roll <= 90:
                multiplier = 0
            elif roll <= 97:
                multiplier = 3
            elif roll <= 99:
                multiplier = 4.5
            else:
                multiplier = 5

            if multiplier > 0:
                winnings = bet * multiplier
                cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id == ?", (winnings, user_id))
                conn.commit()
                await message.reply(f"<blockquote><b>Вы выиграли!</b></blockquote> <u>Выигрыш</u>: +<code>{winnings}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)
            else:
                cursor.execute("UPDATE honey SET honey_count = honey_count - ? WHERE user_id == ?", (bet, user_id))
                conn.commit()
                await message.reply(f"<blockquote><b>Вы проиграли</b></blockquote> <u>Теряете</u>: -<code>{bet}</code> <b>yun-coin</b>", parse_mode=ParseMode.HTML)

    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode=ParseMode.HTML)





@dp.message_handler(Command(["казино", "Казино"], prefixes='!./'))
async def bot_casino(message: types.Message, state: FSMContext):
    if not await check_module(message, 'казино'):
        return
    try:
        user_id = message.from_user.id
        username = message.from_user.username
        cursor.execute("SELECT honey_count FROM honey WHERE user_id == ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            await message.reply(hbold("У вас недостаточно yun-coin"), parse_mode='HTML')
            return

        if result[0] == 0:
            await message.reply(hbold("У вас недостаточно yun-coin для игры в ка��ино."), parse_mode='HTML')
            return

        if len(message.text.split()) == 2 and message.text.split()[1] == "вб":
            bet = result[0] 
        elif len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            bet = int(message.text.split()[1])
        else:
            await message.reply(hbold("Неверный формат ставки. Используйте !казино <��тавка> или !кази��о вб."), parse_mode='HTML')
            return

        if bet > result[0]:
            await message.reply(hbold("У вас недостаточно yun-coin для этой ставки."), parse_mode='HTML')
            return

        is_win = randint(0, 1)  

        if is_win: 
            cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id == ?", (bet, user_id))
            conn.commit()
            await message.reply(f"<blockquote><b>Вы выиграли!</b></blockquote> <u>Получаете</u>: +<code>{bet}</code> <b>yun-coin</b>", parse_mode='HTML')
        else:  
            cursor.execute("UPDATE honey SET honey_count = honey_count - ? WHERE user_id == ?", (bet, user_id))
            conn.commit()
            await message.reply(f"<blockquote><b>Вы проиграли.</b></blockquote> <u>Теряете</u>: -<code>{bet}</code> <b>yun-coin</b>", parse_mode='HTML')

    except Exception as e:
        await message.reply(f"<blockquote><code>{e}</code></blockquote>", parse_mode='HTML')





@dp.message_handler(Command(["Обнулить", "обнулить"], prefixes='!./'))
async def reset_yun_coin(message: types.Message):
    if message.reply_to_message:
        reply_message = message.reply_to_message
        if check_permissions(message.from_user.id):
            try:
                user_id = reply_message.from_user.id
                cursor.execute("UPDATE honey SET honey_count = 0 WHERE user_id = ?", (user_id,))
                conn.commit()

                await message.reply(f'Кошелек {reply_message.from_user.username} был обнулен.')
            except Exception as e:
                await message.reply(f'Произошла ошибка: {e}')
        else:
            await message.reply('У вас нет прав дл�� использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы обнулить его ��чет.')





@dp.message_handler(Command(["Выдать", "выдать"], prefixes='!./'))
async def give_yun_coin(message: types.Message):
    if message.reply_to_message:
        reply_message = message.reply_to_message
        if check_permissions(message.from_user.id):
            try:
                user_id = reply_message.from_user.id
                amount = int(message.text.split()[1])

                if amount < 0:
                    await message.reply('Нельзя выдавать отрицательное количество yun-coin.')
                    return

                cursor.execute("UPDATE honey SET honey_count = honey_count + ? WHERE user_id = ?", (amount, user_id))
                conn.commit()

                await message.reply(f'Выдано {amount} yun-coin на кошелек {reply_message.from_user.username}.')
            except ValueError:
                await message.reply('Некорректное значение количества yun-coin.')
            except Exception as e:
                await message.reply(f'Произошла ошибка: {e}')
        else:
            await message.reply('У вас нет прав для использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы выдать ему yun-coin.')





@dp.message_handler(Command(["Забрать", "забрать"], prefixes='!./'))
async def withdraw_yun_coin(message: types.Message):
    if message.reply_to_message:
        reply_message = message.reply_to_message
        if check_permissions(message.from_user.id):
            try:
                user_id = reply_message.from_user.id
                amount = int(message.text.split()[1])

                if amount < 0:
                    await message.reply('Нельзя забирать отрицательное количество yun-coin.')
                    return

                cursor.execute("UPDATE honey SET honey_count = honey_count - ? WHERE user_id = ?", (amount, user_id))
                conn.commit()

                await message.reply(f'{amount} yun-coin было списано с кошелька {reply_message.from_user.username}.')
            except ValueError:
                await message.reply('Некорректное значение количества yun-coin.')
            except Exception as e:
                await message.reply(f'Произошла ошибка: {e}')
        else:
            await message.reply('У вас нет прав для использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы забрать у него yun-coin.')





@dp.message_handler(Command(["Добавить", "добавить"], prefixes='!./'))
async def add_admin(message: types.Message):
    if message.reply_to_message:
        reply_message = message.reply_to_message
        if message.from_user.id in raz_ids:
            try:
                user_id = reply_message.from_user.id
                if user_id not in admin_ids:
                    cursor.execute("INSERT INTO admin_users (user_id) VALUES (?)", (user_id,))
                    conn.commit()
                    admin_ids.append(user_id)
                    await message.reply(f'Пользователь {reply_message.from_user.username} добавлен в список администраторов.')
                else:
                    await message.reply(f'Пользователь {reply_message.from_user.username} уже является администратором.')
            except Exception as e:
                await message.reply(f'Произола ошибка: {e}')
        else:
            await message.reply('У вас нет прав д��я использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы добавить его в список администраторов.')





@dp.message_handler(Text(equals=['админы', '/админы', '!админы', 'Админы']))
async def show_admins(message: types.Message):
    if check_permissions(message.from_user.id):
        try:
            cursor.execute("SELECT user_id FROM admin_users")
            admins = cursor.fetchall()
            
            if not admins:
                await message.reply("<b>Список администраторов пуст.</b>", parse_mode=ParseMode.HTML)
                return
                
            text = "<b>Администраторы проекта:</b>\n\n"
            for admin_id in admins:
                try:
                    admin_info = await bot.get_chat(admin_id[0])
                    username = admin_info.username or admin_info.first_name
                    text += f"<blockquote>• @{username}</blockquote>\n"
                except:
                    text += f"<blockquote>• ID: {admin_id[0]}</blockquote>\n"
                
            await message.reply(text, parse_mode=ParseMode.HTML)
        except Exception as e:
            await message.reply(f"<b>Произошла ошибка:</b> <code>{e}</code>", parse_mode=ParseMode.HTML)
    else:
        await message.reply("<b>У вас недостаточно привилегий для использования данной команды.</b>\n<blockquote>требуется: администратор/разработчик</blockquote>", parse_mode=ParseMode.HTML)

@dp.message_handler(Text(equals=['.лист']))
async def show_admins(message: types.Message):
    if check_permissions(message.from_user.id):
        try:
            cursor.execute("SELECT user_id FROM admin_users")
            admins = cursor.fetchall()
            
            text = "<b>Системные разработчики:</b>\n"
            for dev_id in raz_ids:
                try:
                    dev_info = await bot.get_chat(dev_id)
                    username = dev_info.username or dev_info.first_name
                    text += f"<blockquote>• @{username}</blockquote>\n"
                except:
                    text += f"<blockquote>• ID: {dev_id}</blockquote>\n"
            
            text += "\n<b>Администраторы проекта:</b>\n"
            if not admins:
                text += "<blockquote>Список администраторов пуст.</blockquote>"
            else:
                for admin_id in admins:
                    if admin_id[0] not in raz_ids:  # Пропускаем разработчиков, так как они уже показаны выше
                        try:
                            admin_info = await bot.get_chat(admin_id[0])
                            username = admin_info.username or admin_info.first_name
                            text += f"<blockquote>• @{username}</blockquote>\n"
                        except:
                            text += f"<blockquote>• ID: {admin_id[0]}</blockquote>\n"
                
            await message.reply(text, parse_mode=ParseMode.HTML)
        except Exception as e:
            await message.reply(f"<b>Произошла ошибка:</b> <code>{e}</code>", parse_mode=ParseMode.HTML)
    else:
        await message.reply("<b>У вас недостаточно привилегий для использования данной команды.</b>\n<blockquote>требуется: администратор/разработчик</blockquote>", parse_mode=ParseMode.HTML)


# Разделяем модули на системные и пользовательские
SYSTEM_MODULES = {
    'бонус': 'Система бонусов',
    'ворк': 'Система работы',
    'шахта': 'Шахта и добыча камней',
    'музыка': 'Поиск музыки',
    'рулетка': 'Игра в рулетку',
    'казино': 'Игра в казино',
    'кнб': 'Камень, ножницы, бумага',
    'элит': 'Элитное казино'
}

USER_MODULES = {
    # Здесь будут пользовательские модули
}

# Обновляем общий список модулей
AVAILABLE_MODULES = {**SYSTEM_MODULES, **USER_MODULES}

@dp.message_handler(Text(equals=['моди', '/м', '!мли']))
async def list_modules(message: types.Message):
    if message.chat.type == 'private':
        await message.reply("<b>Эта команда доступна только в группах!</b>", parse_mode=ParseMode.HTML)
        return
        
    if not check_permissions(message.from_user.id):
        await message.reply("<b>У вас недостаточно прав для управления модулями.</b>", parse_mode=ParseMode.HTML)
        return

    keyboard = InlineKeyboardMarkup(row_width=2)
    sys_btn = InlineKeyboardButton("Системные модули", callback_data="sys_modules")
    user_btn = InlineKeyboardButton("Пользовательские модули [скоро]", callback_data="user_modules")
    keyboard.add(sys_btn, user_btn)

    await message.reply("<b>Выберите категорию модулей:</b>", reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data in ['sys_modules', 'user_modules'])
async def show_modules(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    
    if callback_query.data == 'user_modules':
        if await has_beta_access(chat_id):
            text = "<b>Пользовательские модули</b>\n\n"
            if USER_MODULES:
                text += "<blockquote>Ваши модули:</blockquote>\n"
                keyboard = InlineKeyboardMarkup(row_width=2)
                for module_name, description in USER_MODULES.items():
                    text += f"<blockquote>• {module_name} - {description}</blockquote>\n"
                    info_btn = InlineKeyboardButton(f"ℹ️ {module_name}", callback_data=f"info_{module_name}")
                    keyboard.add(info_btn)
                
                create_btn = InlineKeyboardButton("➕ Создать модуль", callback_data="create_module")
                delete_btn = InlineKeyboardButton("🗑 Удалить модуль", callback_data="delete_module")
                back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
                keyboard.add(create_btn)
                keyboard.add(delete_btn)
                keyboard.add(back_btn)
            else:
                text += "<blockquote>У вас пока нет созданных модулей</blockquote>\n"
                keyboard = InlineKeyboardMarkup(row_width=2)
                create_btn = InlineKeyboardButton("➕ Создать модуль", callback_data="create_module")
                back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
                keyboard.add(create_btn)
                keyboard.add(back_btn)
        else:
            text = "<b>Пользовательские модули</b>\n\n"
            text += "<blockquote>⚠️ Включить бета версию?\n<i>Внимание: функция нестабильна, используйте с осторожностью</i></blockquote>"
            keyboard = InlineKeyboardMarkup(row_width=2)
            enable_btn = InlineKeyboardButton("Включить ⚡️", callback_data="enable_beta")
            back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
            keyboard.add(enable_btn, back_btn)
        
        await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
        return

    modules_dict = SYSTEM_MODULES
    text = "<b>Системные модули:</b>\n\n"
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    for module_name, description in modules_dict.items():
        is_enabled = await is_module_enabled(callback_query.message.chat.id, module_name)
        status = "✅" if is_enabled else "❌"
        text += f"<blockquote>• {module_name} - {description} {status}</blockquote>\n"
        info_btn = InlineKeyboardButton(f"ℹ️ {module_name}", callback_data=f"info_{module_name}")
        keyboard.add(info_btn)
    
    text += "\n<b>Управление:</b>\n"
    text += "<code>!вкл</code> [модуль] - включить модуль\n"
    text += "<code>!выкл</code> [модуль] - выключить модуль"
    
    back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
    keyboard.add(back_btn)
    
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data.startswith("info_"))
async def show_module_info(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await callback_query.answer()  # Сразу отвечаем на callback
        
        module_name = callback_query.data.replace("info_", "")
        module_data = None
        module_type = "Системный" if module_name in SYSTEM_MODULES else "Пользовательский"
        
        if module_name in USER_MODULES:
            cursor.execute('SELECT * FROM user_modules WHERE module_name = ?', (module_name,))
            module_data = cursor.fetchone()
        
        text = f"<b>ℹ️ Информация о модуле '{module_name}'</b>\n\n"
        text += f"<blockquote>🔹 Тип: {module_type}\n"
        
        if module_name in SYSTEM_MODULES:
            text += f"🔹 Описание: {SYSTEM_MODULES[module_name]}\n"
            if module_name == 'шахта':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>зайти в шахту</code> - начать добычу камней\n"
                text += "• <code>переработать</code> - переработать камни в монеты\n"
                text += "• <code>сумка</code> - посмотреть количество камней\n"
            elif module_name == 'кнб':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>/кнб [каме��ь/ножницы/бумага] [ставка]</code>\n"
                text += "• <code>/кнб [выбор] вб</code> - ставка всего баланса\n"
            elif module_name == 'р��летка':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>/рулетка [ставка]</code>\n"
                text += "• <code>/рулетка вб</code> - ставка всего баланса\n"
            elif module_name == 'казино':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>/казино [ставка]</code>\n"
                text += "• <code>/казино вб</code> - ставка всего баланса\n"
            elif module_name == 'элит':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>/элит [ставка]</code> - минимальная ставка 10000\n"
            elif module_name == 'бонус':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>бонус</code> - получить бонус (доступен раз в 3 часа)\n"
            elif module_name == 'ворк':
                text += "\n<b>Команды:</b>\n"
                text += "• <code>ворк</code> - заработать м��неты (доступен раз в 20 минут)\n"
        elif module_data:
            text += f"🔹 Описание: {module_data[2]}\n"
            text += f"🔹 Команды: {module_data[3]}\n"
            text += f"🔹 Тип ответа: {module_data[4]}\n"
            if module_data[4] == 'text':
                text += f"🔹 Текст ответа: {module_data[5]}\n"
            elif module_data[4] == 'photo':
                text += "🔹 Ответ: Фото с подп��сью\n"
            elif module_data[4] == 'buttons':
                text += "🔹 Ответ: Сообщение с кнопками\n"
        
        is_enabled = await is_module_enabled(callback_query.message.chat.id, module_name)
        text += f"\n🔹 Сатус: {'Включен ✅' if is_enabled else 'Выключен ❌'}</blockquote>"
        
        keyboard = InlineKeyboardMarkup(row_width=2)
        if not is_enabled:
            enable_btn = InlineKeyboardButton("✅ Включить", callback_data=f"enable_{module_name}")
            keyboard.add(enable_btn)
        else:
            disable_btn = InlineKeyboardButton("❌ Выключить", callback_data=f"disable_{module_name}")
            keyboard.add(disable_btn)
        
        back_btn = InlineKeyboardButton("↩️ Назад", callback_data="sys_modules" if module_name in SYSTEM_MODULES else "user_modules")
        keyboard.add(back_btn)
        
        await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    except Exception as e:
        await callback_query.answer(f"Произошла ошибка: {str(e)}", show_alert=True)

@dp.callback_query_handler(lambda c: c.data.startswith(("enable_", "disable_")))
async def toggle_module(callback_query: types.CallbackQuery):
    action, module_name = callback_query.data.split("_")
    if not check_permissions(callback_query.from_user.id):
        await callback_query.answer("У вас нет прав для управления модулями!", show_alert=True)
        return
    
    is_enabled = action == "enable"
    cursor.execute('INSERT OR REPLACE INTO modules (chat_id, module_name, is_enabled) VALUES (?, ?, ?)',
                  (callback_query.message.chat.id, module_name, int(is_enabled)))
    conn.commit()
    
    await callback_query.answer(f"Модуль {module_name} {'включен' if is_enabled else 'выключен'}!")
    await show_module_info(callback_query, None)

@dp.callback_query_handler(lambda c: c.data == "back_to_modules")
async def back_to_modules_menu(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2)
    sys_btn = InlineKeyboardButton("Системные модули", callback_data="sys_modules")
    user_btn = InlineKeyboardButton("Пользовательские модули [скоро]", callback_data="user_modules")
    keyboard.add(sys_btn, user_btn)
    
    await callback_query.message.edit_text("<b>Выберите категорию модулей:</b>", 
                                         reply_markup=keyboard, 
                                         parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "enable_beta")
async def enable_beta(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    cursor.execute('INSERT OR REPLACE INTO beta_access (chat_id, enabled) VALUES (?, 1)', (chat_id,))
    conn.commit()
    
    text = "<b>⚡️ Бета версия активирована!</b>\n\n"
    text += "<blockquote>🎉 Поздравляем! Теперь у вас есть доступ к пользовательским модулям.\nОбратите вниман��е: функции находятся в разработке и могут работать нестабильно.</blockquote>"
    keyboard = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
    keyboard.add(back_btn)
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

# Модифицируем существующие обработчики команд, добавляя проверку модуля
async def check_module(message: types.Message, module_name: str) -> bool:
    if not await is_module_enabled(message.chat.id, module_name):
        await message.reply(f"<b>Модуль '{module_name}' отключен в этом чате.</b>", parse_mode=ParseMode.HTML)
        return False
    return True

async def is_module_enabled(chat_id: int, module_name: str) -> bool:
    cursor.execute('SELECT is_enabled FROM modules WHERE chat_id = ? AND module_name = ?', (chat_id, module_name))
    result = cursor.fetchone()
    if result is None:
        cursor.execute('INSERT INTO modules (chat_id, module_name, is_enabled) VALUES (?, ?, 1)', (chat_id, module_name))
        conn.commit()
        return True
    return bool(result[0])

@dp.message_handler(commands=['вкл'])
async def enable_module(message: types.Message):
    if message.chat.type == 'private':
        await message.reply("<b>Эта команда доступна только в группах!</b>", parse_mode=ParseMode.HTML)
        return
        
    if not check_permissions(message.from_user.id):
        await message.reply("<b>У вас недостаточно прав для управления модулями.</b>", parse_mode=ParseMode.HTML)
        return

    args = message.text.split()
    if len(args) != 2:
        await message.reply("<b>Использование:</b> <code>/вкл название_модуля</code>", parse_mode=ParseMode.HTML)
        return

    module_name = args[1].lower()
    if module_name not in AVAILABLE_MODULES:
        modules_list = "\n".join([f"• {name}" for name in AVAILABLE_MODULES.keys()])
        await message.reply(f"<b>Модуль '{module_name}' не найден.</b>\n\n<b>Доступные модули:</b>\n{modules_list}", parse_mode=ParseMode.HTML)
        return

    cursor.execute('INSERT OR REPLACE INTO modules (chat_id, module_name, is_enabled) VALUES (?, ?, 1)',
                  (message.chat.id, module_name))
    conn.commit()
    await message.reply(f"<b>Модуль '{module_name}' включен.</b>", parse_mode=ParseMode.HTML)

@dp.message_handler(commands=['выкл'])
async def disable_module(message: types.Message):
    if message.chat.type == 'private':
        await message.reply("<b>Эта команда доступна только в группах!</b>", parse_mode=ParseMode.HTML)
        return
        
    if not check_permissions(message.from_user.id):
        await message.reply("<b>У вас недостато��но прав для управления модулями.</b>", parse_mode=ParseMode.HTML)
        return

    args = message.text.split()
    if len(args) != 2:
        await message.reply("<b>Использование:</b> <code>/выкл названи��_модуля</code>", parse_mode=ParseMode.HTML)
        return

    module_name = args[1].lower()
    if module_name not in AVAILABLE_MODULES:
        modules_list = "\n".join([f"• {name}" for name in AVAILABLE_MODULES.keys()])
        await message.reply(f"<b>Модуль '{module_name}' не найден.</b>\n\n<b>Доступн��е модули:</b>\n{modules_list}", parse_mode=ParseMode.HTML)
        return

    cursor.execute('INSERT OR REPLACE INTO modules (chat_id, module_name, is_enabled) VALUES (?, ?, 0)',
                  (message.chat.id, module_name))
    conn.commit()
    await message.reply(f"<b>Модуль '{module_name}' выключен.</b>", parse_mode=ParseMode.HTML)

@dp.message_handler(Command(['вкл', 'выкл'], prefixes='!./'))
async def handle_module_command(message: types.Message):
    command = message.text.split()[0][1:] # убираем префикс
    if command == 'вкл':
        await enable_module(message)
    else:
        await disable_module(message)

@dp.message_handler(Text(equals=['зайти в шахту', 'шахта', '/шахта', '!шахта']))
async def mine_stones(message: types.Message):
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return

    if not await check_module(message, 'шахта'):
        return

    keyboard = InlineKeyboardMarkup()
    mine_btn = InlineKeyboardButton("⛏ Копать", callback_data="mine_stones")
    keyboard.add(mine_btn)
    
    await message.reply("<b>⛰ Добро пожаловать в шахту!</b>\n<blockquote>Нажмите на кнопку, чтобы начать добычу.</blockquote>", 
                       reply_markup=keyboard, 
                       parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "mine_stones")
async def mine_stones_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    stones_found = random.randint(1, 5)
    
    cursor.execute('SELECT stones FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    if user:
        new_stones = user[0] + stones_found
        cursor.execute('UPDATE users SET stones = ? WHERE user_id = ?', (new_stones, user_id))
    else:
        cursor.execute('INSERT INTO users (user_id, stones) VALUES (?, ?)', 
                      (user_id, stones_found))
    
    conn.commit()

    keyboard = InlineKeyboardMarkup()
    mine_btn = InlineKeyboardButton("⛏ Копать ещё", callback_data="mine_stones")
    keyboard.add(mine_btn)
    
    await callback_query.message.edit_text(
        f"<b>⛰ Шахта</b>\n<blockquote>🎉 Вы нашли {stones_found} камней!</blockquote>",
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )

@dp.message_handler(Text(equals=['переработать', '/переработать', '!переработать']))
async def process_stones(message: types.Message):
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return

    if not await check_module(message, 'шахта'):
        return

    user_id = message.from_user.id
    
    cursor.execute('SELECT stones FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    if not user or user[0] == 0:
        await message.reply("<blockquote>У вас нет камней для переработки!</blockquote>", parse_mode=ParseMode.HTML)
        return
    
    stones = user[0]
    coins = stones * 2  # Каждый камень даёт 2 монеты
    
    cursor.execute('UPDATE users SET stones = 0 WHERE user_id = ?', (user_id,))
    cursor.execute('SELECT honey_count FROM honey WHERE user_id = ?', (user_id,))
    honey_record = cursor.fetchone()
    
    if honey_record:
        new_honey = honey_record[0] + coins
        cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (new_honey, user_id))
    else:
        cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (user_id, coins))
    
    conn.commit()
    await message.reply(f"<blockquote>Вы переработали {stones} камней и получили {coins} yun-coin!</blockquote>", parse_mode=ParseMode.HTML)

@dp.message_handler(Text(equals=['сумка', '/сумка', '!сумка']))
async def show_backpack(message: types.Message):
    if message.chat.type != 'private':
        await message.reply("<b>Эта команда доступна только в личных сообщениях с ботом!</b>", parse_mode=ParseMode.HTML)
        return

    if not await check_module(message, 'шахта'):
        return

    user_id = message.from_user.id
    cursor.execute('SELECT stones FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    if not user:
        stones = 0
    else:
        stones = user[0]
    
    await message.reply(f"<blockquote>В вашей сумке {stones} камней</blockquote>", parse_mode=ParseMode.HTML)

async def has_beta_access(chat_id: int) -> bool:
    cursor.execute('SELECT enabled FROM beta_access WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()
    return bool(result[0]) if result else False

class ModuleCreation(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_commands = State()
    waiting_for_response_type = State()
    waiting_for_text = State()
    waiting_for_photo = State()
    waiting_for_buttons = State()
    waiting_for_confirmation = State()

@dp.callback_query_handler(lambda c: c.data == "create_module")
async def create_module_menu(callback_query: types.CallbackQuery):
    text = "<b>🛠 Создание пользовательского модуля</b>\n\n"
    text += "<blockquote>Выберите тип модуля, который хотите создать:</blockquote>"
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    game_btn = InlineKeyboardButton("🎮 Игровой", callback_data="create_game_module")
    util_btn = InlineKeyboardButton("🔧 Утилита", callback_data="create_util_module")
    back_btn = InlineKeyboardButton("↩️ Назад", callback_data="user_modules")
    
    keyboard.add(game_btn, util_btn)
    keyboard.add(back_btn)
    
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data.startswith("create_"))
async def start_module_creation(callback_query: types.CallbackQuery, state: FSMContext):
    module_type = callback_query.data.replace("create_", "")
    
    if module_type not in ["game_module", "util_module"]:
        await callback_query.answer("Неверный тип модуля!", show_alert=True)
        return
        
    await ModuleCreation.waiting_for_name.set()
    await state.update_data(module_type=module_type)
    
    text = "<b>📝 Создание модуля - Шаг 1/3</b>\n\n"
    text += "<blockquote>Введите название вашего модуля (например: 'мини-игра' или 'калькулятор'):</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(cancel_btn)
    
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message_handler(state=ModuleCreation.waiting_for_name)
async def process_module_name(message: types.Message, state: FSMContext):
    module_name = message.text.lower()
    
    if module_name in AVAILABLE_MODULES:
        await message.reply("<b>❌ Модуль с таким названием уже существует. Пожалуйста, выберите другое название.</b>", parse_mode=ParseMode.HTML)
        return
        
    await state.update_data(module_name=module_name)
    await ModuleCreation.waiting_for_description.set()
    
    text = "<b>📝 Создание модуля - Шаг 2/3</b>\n\n"
    text += "<blockquote>Введите описание вашего модуля:</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(cancel_btn)
    
    await message.reply(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message_handler(state=ModuleCreation.waiting_for_description)
async def process_module_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await ModuleCreation.waiting_for_commands.set()
    
    text = "<b>📝 Создание модуля - Шаг 3/3</b>\n\n"
    text += "<blockquote>Введите команды для вашего модуля через запятую\n(например: !игра, /игра, игра):</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(cancel_btn)
    
    await message.reply(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message_handler(state=ModuleCreation.waiting_for_commands)
async def process_module_commands(message: types.Message, state: FSMContext):
    commands = [cmd.strip() for cmd in message.text.split(',')]
    await state.update_data(commands=commands)
    
    text = "<b>📝 Настройка ответа модуля</b>\n\n"
    text += "<blockquote>Выберите тип ответа для вашего модуля:</blockquote>"
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    text_btn = InlineKeyboardButton("📝 Текст", callback_data="response_text")
    photo_btn = InlineKeyboardButton("🖼 Фото + текст", callback_data="response_photo")
    buttons_btn = InlineKeyboardButton("🔘 Кнопки", callback_data="response_buttons")
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    
    keyboard.add(text_btn, photo_btn)
    keyboard.add(buttons_btn)
    keyboard.add(cancel_btn)
    
    await ModuleCreation.waiting_for_response_type.set()
    await message.reply(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "cancel_creation", state="*")
async def cancel_module_creation(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await create_module_menu(callback_query)

@dp.callback_query_handler(lambda c: c.data.startswith("response_"), state=ModuleCreation.waiting_for_response_type)
async def process_response_type(callback_query: types.CallbackQuery, state: FSMContext):
    response_type = callback_query.data.replace("response_", "")
    await state.update_data(response_type=response_type)
    
    if response_type == "text":
        text = "<b>📝 Введите текст ответа</b>\n\n"
        text += "<blockquote>Поддерживается HTML-разметка:\n"
        text += "• &lt;b&gt;жирный&lt;/b&gt;\n"
        text += "• &lt;i&gt;курсив&lt;/i&gt;\n"
        text += "• &lt;code&gt;моноширинный&lt;/code&gt;\n"
        text += "• &lt;blockquote&gt;цитата&lt;/blockquote&gt;</blockquote>"
    elif response_type == "photo":
        text = "<b>🖼 Отправьте фото</b>\n\n"
        text += "<blockquote>После отправки фото вы сможете добавить к нему подпись.</blockquote>"
    else:  # buttons
        text = "<b>🔘 Настройка кнопок</b>\n\n"
        text += "<blockquote>Введите кнопки в формате:\n"
        text += "текст1 = ссылка1\n"
        text += "текст2 = ссылка2\n"
        text += "текст3</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(cancel_btn)
    
    await ModuleCreation.waiting_for_text.set()
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message_handler(state=ModuleCreation.waiting_for_text, content_types=['text', 'photo'])
async def process_response_content(message: types.Message, state: FSMContext):
    data = await state.get_data()
    response_type = data.get('response_type')
    
    if response_type == "photo" and not message.photo:
        await message.reply("<b>❌ Пожалуйста, отправьте фото.</b>", parse_mode=ParseMode.HTML)
        return
    
    if response_type == "photo":
        photo_file_id = message.photo[-1].file_id
        await state.update_data(photo=photo_file_id)
        text = "<b>📝 Теперь введите подпись к фото</b>"
        await ModuleCreation.waiting_for_text.set()
    elif response_type == "buttons":
        buttons = []
        for line in message.text.split('\n'):
            if '=' in line:
                text, url = line.split('=', 1)
                buttons.append({"text": text.strip(), "url": url.strip()})
            else:
                buttons.append({"text": line.strip()})
        await state.update_data(buttons=buttons)
    
    await state.update_data(text=message.text)
    
    # Показываем предпросмотр
    text = "<b>📋 Подтверждение создания модуля</b>\n\n"
    text += f"<blockquote>Тип: {'🎮 Игровой' if data['module_type'] == 'game_module' else '🔧 Утилита'}\n"
    text += f"Название: {data['module_name']}\n"
    text += f"Описание: {data['description']}\n"
    text += f"Команды: {', '.join(data['commands'])}\n"
    text += f"Тип ответа: {response_type}</blockquote>"
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    confirm_btn = InlineKeyboardButton("✅ Подтвердить", callback_data="confirm_module")
    add_command_btn = InlineKeyboardButton("➕ Добавить команду", callback_data="add_command")
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(confirm_btn, add_command_btn)
    keyboard.add(cancel_btn)
    
    await ModuleCreation.waiting_for_confirmation.set()
    await message.reply(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "confirm_module", state=ModuleCreation.waiting_for_confirmation)
async def confirm_module_creation(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    module_name = data['module_name']
    description = data['description']
    module_type = data['module_type']
    commands = ','.join(data['commands'])
    response_type = data.get('response_type', 'text')
    response_data = data.get('text', '')
    
    if response_type == 'photo':
        response_data = f"{data.get('photo', '')}|{data.get('text', '')}"
    elif response_type == 'buttons':
        response_data = str(data.get('buttons', []))
    
    # Сохраняем модуль в базу данных
    cursor.execute('''
        INSERT OR REPLACE INTO user_modules 
        (module_name, module_type, description, commands, response_type, response_data) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (module_name, module_type, description, commands, response_type, response_data))
    conn.commit()
    
    # Обновляем локальные переменные
    USER_MODULES[module_name] = description
    AVAILABLE_MODULES.update(USER_MODULES)
    
    await state.finish()
    
    text = "<b>✅ Модуль успешно создан!</b>\n\n"
    text += "<blockquote>Теперь вы можете включить его в настройках модулей.</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton("↩️ К модулям", callback_data="user_modules")
    keyboard.add(back_btn)
    
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "add_command", state=ModuleCreation.waiting_for_confirmation)
async def add_command(callback_query: types.CallbackQuery, state: FSMContext):
    text = "<b>➕ Добавление команды</b>\n\n"
    text += "<blockquote>Введите дополнительные команды через запятую\n(например: !игра2, /игра2, игра2):</blockquote>"
    
    keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_add_command")
    keyboard.add(cancel_btn)
    
    await ModuleCreation.waiting_for_commands.set()
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data == "cancel_add_command", state=ModuleCreation.waiting_for_commands)
async def cancel_add_command(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    
    text = "<b>📋 Подтверждение создания модуля</b>\n\n"
    text += f"<blockquote>Тип: {'🎮 Игровой' if data['module_type'] == 'game_module' else '🔧 Утилита'}\n"
    text += f"Название: {data['module_name']}\n"
    text += f"Описание: {data['description']}\n"
    text += f"Команды: {', '.join(data['commands'])}</blockquote>"
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    confirm_btn = InlineKeyboardButton("✅ Подтвердить", callback_data="confirm_module")
    add_command_btn = InlineKeyboardButton("➕ Добавить команду", callback_data="add_command")
    cancel_btn = InlineKeyboardButton("❌ Отмена", callback_data="cancel_creation")
    keyboard.add(confirm_btn, add_command_btn)
    keyboard.add(cancel_btn)
    
    await ModuleCreation.waiting_for_confirmation.set()
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.callback_query_handler(lambda c: c.data.startswith("delete_"))
async def delete_selected_module(callback_query: types.CallbackQuery):
    if not check_permissions(callback_query.from_user.id):
        await callback_query.answer("У вас нет прав для удаления модулей!", show_alert=True)
        return
        
    module_name = callback_query.data.replace("delete_", "")
    
    if module_name in USER_MODULES:
        # Удаляем модуль из базы данных
        cursor.execute('DELETE FROM user_modules WHERE module_name = ?', (module_name,))
        cursor.execute('DELETE FROM modules WHERE module_name = ?', (module_name,))
        conn.commit()
        
        # Удаляем из локальных переменных
        del USER_MODULES[module_name]
        if module_name in AVAILABLE_MODULES:
            del AVAILABLE_MODULES[module_name]
        
        text = "<b>✅ Модуль успешно удален!</b>\n\n"
        text += "<blockquote>Все настройки и данные модуля были очищены.</blockquote>"
        
        keyboard = InlineKeyboardMarkup()
        back_btn = InlineKeyboardButton("↩️ К модулям", callback_data="user_modules")
        keyboard.add(back_btn)
        
        await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    else:
        await callback_query.answer("Модуль не найден!", show_alert=True)

# Загружаем пользовательские модули при запуске
cursor.execute('SELECT * FROM user_modules')
modules = cursor.fetchall()
for module in modules:
    USER_MODULES[module[0]] = module[2]
    AVAILABLE_MODULES.update(USER_MODULES)

@dp.message_handler()
async def handle_user_modules(message: types.Message):
    # Получаем все пользовательские модули
    cursor.execute('SELECT * FROM user_modules')
    modules = cursor.fetchall()
    
    for module in modules:
        module_name = module[0]
        commands = module[3].split(',')
        response_type = module[4]
        response_data = module[5]
        
        # Проверяем, соответствует ли сообщение какой-либо команде модуля
        if message.text.lower() in [cmd.strip().lower() for cmd in commands]:
            # Проверяем, включен ли модуль
            if not await check_module(message, module_name):
                return
                
            # Отправляем ответ в зависимости от типа
            if response_type == 'text':
                await message.reply(response_data, parse_mode=ParseMode.HTML)
            
            elif response_type == 'photo':
                photo_id, caption = response_data.split('|')
                await message.reply_photo(photo_id, caption=caption, parse_mode=ParseMode.HTML)
            
            elif response_type == 'buttons':
                keyboard = InlineKeyboardMarkup(row_width=2)
                buttons = eval(response_data)  # Преобразуем строку в список словарей
                
                for button in buttons:
                    if 'url' in button:
                        btn = InlineKeyboardButton(button['text'], url=button['url'])
                    else:
                        btn = InlineKeyboardButton(button['text'], callback_data=f"custom_{module_name}_{button['text']}")
                    keyboard.add(btn)
                
                await message.reply("Выберите действие:", reply_markup=keyboard, parse_mode=ParseMode.HTML)
            
            return  # Прерываем обработку, если команда найдена

@dp.callback_query_handler(lambda c: c.data.startswith("custom_"))
async def handle_custom_button(callback_query: types.CallbackQuery):
    try:
        _, module_name, button_text = callback_query.data.split('_', 2)
        await callback_query.answer(f"Нажата кнопка '{button_text}' модуля '{module_name}'")
    except Exception as e:
        await callback_query.answer(f"Ошибка: {str(e)}", show_alert=True)

@dp.message_handler(Text(equals=['!удалить всех админов нахуй']))
async def remove_all_admins(message: types.Message):
    if message.from_user.id not in raz_ids:
        await message.reply("<b>У вас нет прав для использования этой команды.</b>\n<blockquote>требуется: разработчик</blockquote>", parse_mode=ParseMode.HTML)
        return
        
    try:
        # Получаем список всех админов
        cursor.execute("SELECT user_id FROM admin_users")
        admins = cursor.fetchall()
        
        if not admins:
            await message.reply("<b>Список администраторов уже пуст.</b>", parse_mode=ParseMode.HTML)
            return
            
        # Очищаем таблицу админов
        cursor.execute("DELETE FROM admin_users")
        conn.commit()
        
        # Очищаем список админов в памяти
        admin_ids.clear()
        
        # Добавляем обратно разработчиков
        for dev_id in raz_ids:
            if dev_id not in admin_ids:
                cursor.execute("INSERT OR IGNORE INTO admin_users (user_id) VALUES (?)", (dev_id,))
                admin_ids.append(dev_id)
        conn.commit()
        
        await message.reply("<b>✅ Все администраторы успешно удалены!</b>\n<blockquote>Остались только разработчики.</blockquote>", parse_mode=ParseMode.HTML)
        
    except Exception as e:
        await message.reply(f"<b>Произошла ошибка:</b> <code>{e}</code>", parse_mode=ParseMode.HTML)

@dp.message_handler(Text(startswith=['невия', 'Невия']))
async def nevia_ai(message: types.Message):
    try:
        # Получаем текст после команды
        query = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else None
        
        if not query:
            await message.reply("<b>Использование:</b> <code>невия [ваш вопрос]</code>", parse_mode=ParseMode.HTML)
            return

        # Получаем историю чата пользователя (последние 5 сообщений)
        cursor.execute('''
            SELECT message, response FROM chat_history 
            WHERE user_id = ? 
            ORDER BY timestamp DESC LIMIT 5
        ''', (message.from_user.id,))
        
        history = cursor.fetchall()
        
        # Формируем контекст из истории
        context = ""
        if history:
            for msg, resp in history:
                context += f"Human: {msg}\nAssistant: {resp}\n"
        
        # Формируем промпт с историей
        prompt = f"{context}Human: {query}\nAssistant:"
        
        # Отправляем сообщение о генерации
        processing_msg = await message.reply("<b>🤔 Генерирую ответ...</b>", parse_mode=ParseMode.HTML)
        
        try:
            # Используем g4f для генерации ответа
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                provider=g4f.Provider.DeepAi,
            )
            
            # Сохраняем сообщение и ответ в историю
            cursor.execute('''
                INSERT INTO chat_history (user_id, message, response) 
                VALUES (?, ?, ?)
            ''', (message.from_user.id, query, response))
            conn.commit()
            
            # Редактируем сообщение с ответом
            await processing_msg.edit_text(f"<b>🤖 Ответ:</b>\n\n<blockquote>{response}</blockquote>", parse_mode=ParseMode.HTML)
            
        except Exception as e:
            await processing_msg.edit_text(f"<b>Произошла ошибка при генерации:</b> <code>{str(e)}</code>", parse_mode=ParseMode.HTML)
            
    except Exception as e:
        await message.reply(f"<b>Произошла ошибк��:</b> <code>{str(e)}</code>", parse_mode=ParseMode.HTML)

@dp.message_handler(Text(equals=['.очистить историю', '.clear']))
async def clear_chat_history(message: types.Message):
    if not check_permissions(message.from_user.id):
        await message.reply("<b>У вас ��ет прав для исполь��ования этой команды.</b>", parse_mode=ParseMode.HTML)
        return
        
    try:
        cursor.execute('DELETE FROM chat_history WHERE user_id = ?', (message.from_user.id,))
        conn.commit()
        await message.reply("<b>✅ История чата успешно очищена!</b>", parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply(f"<b>Произошла ошибка:</b> <code>{str(e)}</code>", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
