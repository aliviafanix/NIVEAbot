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

from aiogram import Bot, Dispatcher, executor, types
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
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import ChatNotFound

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
        elif platform.system() == "Darwin": # macOS
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

        text = f"""Сервер: {server_name}
Задержка: {latency:.4f} секc
Задержка: {latency_ms:.2f} мсекc
Время работы: {uptime_days} дн, {uptime_hours} ч, {uptime_minutes} мин, {uptime_seconds} сек
Возможная задержка: {possible_latency} сек"""

        await message.answer(text)
    except Exception as e:
        await message.answer(f"Ошибка: {e}")


async def main():
    await dp.start_polling()

class SaveMessages(StatesGroup):
    saving = State()

raz_ids = [6558424230, 6998521871, 5932424109]
admin_ids = []

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
        stones INTEGER DEFAULT 0,
        username TEXT
    )
''')



cursor.execute('PRAGMA table_info(honey)')
columns = cursor.fetchall()
theme_exists = any(column[1] == 'theme' for column in columns)

if not theme_exists:
    cursor.execute("ALTER TABLE honey ADD COLUMN theme TEXT DEFAULT 'стандарт'")
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
<blockquote><b>фарм ваших yun-coin, в двух командах присутствует тайм взаимодействия, в 3 часа от бонуса, и 20 минут от ворка.</b></blockquote>
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
        if current_theme == 'стандарт':
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
            await message.reply(f"Вы уже забрали бонус недавно. <blockquote>Вы сможете собрать снова через {hours} часов, {minutes} минут и {seconds} секунд.</blockquote>", parse_mode=ParseMode.HTML)
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
            await message.reply("Некорректный формат команды. <blockquote>Используйте: 'отдать <число>'.</blockquote>", parse_mode=ParseMode.HTML)
    else:
        await message.reply("<b>Вы не выбрали пользователя для передачи.</b>", parse_mode=ParseMode.HTML)





@dp.message_handler(commands=["кнб", "Кнб"], commands_prefix='!./')
async def bot_rps(message: types.Message):
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
    try:
        user_id = message.from_user.id
        username = message.from_user.username
        cursor.execute("SELECT honey_count FROM honey WHERE user_id == ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            await message.reply(hbold("У вас недостаточно yun-coin"), parse_mode='HTML')
            return

        if result[0] == 0:
            await message.reply(hbold("У вас недостаточно yun-coin для игры в казино."), parse_mode='HTML')
            return

        if len(message.text.split()) == 2 and message.text.split()[1] == "вб":
            bet = result[0] 
        elif len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            bet = int(message.text.split()[1])
        else:
            await message.reply(hbold("Неверный формат ставки. Используйте !казино <ставка> или !казино вб."), parse_mode='HTML')
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
            await message.reply('У вас нет прав для использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы обнулить его счет.')





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
            await message.reply('У вас нет прав для использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы добавить его в список администраторов.')





@dp.message_handler(Command(["удалить", "Удалить"], prefixes='!./'))
async def remove_admin(message: types.Message):
    if message.reply_to_message:
        reply_message = message.reply_to_message
        if message.from_user.id in raz_ids:
            try:
                user_id = reply_message.from_user.id
                if user_id in admin_ids:
                    cursor.execute("DELETE FROM admin_users WHERE user_id = ?", (user_id,))
                    conn.commit()
                    admin_ids.remove(user_id)
                    await message.reply(f'Пользователь {reply_message.from_user.username} удален из списка администраторов.')
                else:
                    await message.reply(f'Пользователь {reply_message.from_user.username} не является администратором.')
            except Exception as e:
                await message.reply(f'Произола ошибка: {e}')
        else:
            await message.reply('У вас нет прав для использования этой команды.')
    else:
        await message.reply('Вы должны ответить на сообщение пользователя, чтобы удалить его из списка администраторов.')






@dp.message_handler(lambda message: message.text.lower() == 'зайти в шахту' and message.chat.type == 'private', state=None)
async def enter_mine(message: types.Message):
    await message.reply("<blockquote>вы зашли в шахту</blockquote> <b>собирайте камни чтобы их переработать в коины.</b>", parse_mode=ParseMode.HTML, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("собрать камни", callback_data="dig")))


@dp.callback_query_handler(lambda c: c.data == "dig")
async def dig(call: types.CallbackQuery):
    await call.message.edit_text("Вы начали собирать...")
    user_id = call.from_user.id
    stones_count = random.randint(5, 20)
    await call.message.edit_text(f"<blockquote><b>+{stones_count} камней в сумку.</b></blockquote>", parse_mode=ParseMode.HTML, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("обрать камни", callback_data="dig")))
    await add_stones(user_id, stones_count)

@dp.message_handler(lambda message: message.text.lower() == "сумка", state=None)
async def check_stones(message: types.Message):
    user_id = message.from_user.id
    stones_count = await get_user_stones(user_id)
    await message.reply(f"<b>В вашей сумке</b> <blockquote>камней: {stones_count}</blockquote>", parse_mode=ParseMode.HTML)



@dp.message_handler(lambda message: message.text.lower() == "переработать", state=None)
async def recycle_stones(message: types.Message):
    user_id = message.from_user.id
    stones_count = await get_user_stones(user_id)
    if stones_count == 0:
        await message.reply("<b>У вас нет камней для переработки.</b>", parse_mode=ParseMode.HTML)
        return




    yun_coins = stones_count * 2
    await add_yun_coins(user_id, yun_coins)
    await message.reply(f"<blockquote>Вы переработали {stones_count} камней</blockquote>\n<b>и получили {yun_coins} yun-coin</b>", parse_mode=ParseMode.HTML)
    await update_user_stones(user_id, 0) 

async def add_stones(user_id, stones_count):
    cursor.execute('SELECT stones FROM users WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()
    if record:
        current_stones = record[0]
        new_stones = current_stones + stones_count
        cursor.execute('UPDATE users SET stones = ? WHERE user_id = ?', (new_stones, user_id))
    else:
        cursor.execute('INSERT INTO users (user_id, stones) VALUES (?, ?)', (user_id, stones_count))
    conn.commit()

async def get_user_stones(user_id):
    cursor.execute('SELECT stones FROM users WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()
    if record:
        return record[0]
    else:
        return 0

async def update_user_stones(user_id, stones_count):
    cursor.execute('UPDATE users SET stones = ? WHERE user_id = ?', (stones_count, user_id))
    conn.commit()

async def add_yun_coins(user_id, yun_coins):
    cursor.execute('SELECT honey_count FROM honey WHERE user_id = ?', (user_id,))
    record = cursor.fetchone()
    if record:
        current_yun_coins = record[0]
        new_yun_coins = current_yun_coins + yun_coins
        cursor.execute('UPDATE honey SET honey_count = ? WHERE user_id = ?', (new_yun_coins, user_id))
    else:
        cursor.execute('INSERT INTO honey (user_id, honey_count) VALUES (?, ?)', (user_id, yun_coins 
))
    conn.commit()

@dp.message_handler(lambda message: message.text.lower() == 'зайти в шахту' and message.chat.type != 'private', state=None)
async def handle_command_in_group(message: types.Message):
    user_id = message.from_user.id
    bot_info = await message.bot.get_me()
    bot_username = bot_info.username  

    await message.reply(f"<b><u>Эта команда доступна только в личных сообщениях.</u></b>", parse_mode=ParseMode.HTML, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Личный чат", url=f"t.me/{bot_username}")))




from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup
import asyncio


def search_all_services(query):
    search_results = []
    services = {
        'VK Music 🎵': 'https://vk.com/music/search/',
        'Yandex Music 🎧': 'https://music.yandex.ru/search/',
        'SoundCloud 🌊': 'https://soundcloud.com/search/',
        'Spotify 💚': 'https://open.spotify.com/search/',
        'Apple Music 🍎': 'https://music.apple.com/search/',
        'Deezer 💿': 'https://www.deezer.com/search/',
        'YouTube Music 🎥': 'https://music.youtube.com/search/',
        'Amazon Music 📦': 'https://music.amazon.com/search/'
    }
    
    for service_name, base_url in services.items():
        try:
            url = f"{base_url}{query}"
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Accept': 'text/html,application/xhtml+xml'
            }
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                search_results.append({
                    'service': service_name,
                    'url': url,
                    'status': 'found'
                })
        except:
            continue
            
    return search_results

def search_zaycev(query):
    url = f"https://zaycev.net/search.html?query_search={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tracks = []
    
    for track in soup.find_all('div', class_='musicset-track__title')[:5]:
        title = track.text.strip()
        artist = track.find_next('div', class_='musicset-track__artist').text.strip()
        url = track.find_parent('div', class_='musicset-track')['data-url']
        tracks.append({
            'title': title,
            'artist': artist,
            'url': url
        })
    return tracks

def search_muzofond(query):
    url = f"https://muzofond.fm/search/{query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tracks = []
    
    for track in soup.find_all('div', class_='item')[:5]:
        title = track.find('div', class_='title').text.strip()
        artist = track.find('div', class_='artist').text.strip()
        url = track['data-url']
        tracks.append({
            'title': title,
            'artist': artist,
            'url': url
        })
    return tracks

def search_mp3party(query):
    url = f"https://mp3party.net/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tracks = []
    
    for track in soup.find_all('div', class_='track-item')[:5]:
        title = track.find('div', class_='title').text.strip()
        artist = track.find('div', class_='artist').text.strip()
        url = track['data-mp3']
        tracks.append({
            'title': title,
            'artist': artist,
            'url': url
        })
    return tracks

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "👋 Привет! Я музыкальный бот-агрегатор.\n"
        "Используй команду /музыка название_песни чтобы найти музыку во всех сервисах!"
    )

@dp.message_handler(commands=['музыка'])
async def music_search(message: types.Message):
    query = message.text.replace('/музыка', '').strip()
    
    if not query:
        await message.reply("🎵 Введите название песни после команды /музыка")
        return

    status_message = await message.reply("🔍 Ищу во всех музыкальных сервисах...")
    
    try:
        # Поиск по стриминговым сервисам
        results = search_all_services(query)
        
        if results:
            response_text = f"🎵 Результаты поиска '{query}':\n\n"
            
            # Создаем клавиатуру с кнопками сервисов
            keyboard = InlineKeyboardMarkup(row_width=2)
            for result in results:
                keyboard.insert(InlineKeyboardButton(
                    text=result['service'],
                    url=result['url']
                ))
                response_text += f"{result['service']}\n"
            
            await status_message.edit_text(
                response_text,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )
            
            # Параллельный поиск и отправка треков
            download_services = {
                'Zaycev': search_zaycev,
                'Muzofond': search_muzofond,
                'MP3Party': search_mp3party
            }
            
            for service_name, search_func in download_services.items():
                try:
                    tracks = search_func(query)
                    if tracks:
                        track = tracks[0]
                        response = requests.get(track['url'])
                        await message.reply_audio(
                            response.content,
                            title=track['title'],
                            performer=track['artist'],
                            caption=f"🎵 {track['artist']} - {track['title']}\n📀 Найдено в {service_name}"
                        )
                except:
                    continue
                    
        else:
            await status_message.edit_text("😕 Ничего не найдено")
            
    except Exception as e:
        await status_message.edit_text("😔 Ошибка при поиске")










# Initialize chat history dictionary
chat_history = {}

# System prompt that will be enforced
SYSTEM_PROMPT = {"role": "system", "content": "не пиши про фильмы книги и тд.Привет,ты девшука пиши в нежном стиле и всегда в женском рлде веть   ты Невия женщина именно нежная женщина мечта любого!отвечай кратко и иногда как будто  не попадай по буквам,модешь использовать маты,пиши как реальный пользователь телеграм - не осень большие сообщения,не используй емодзи,ты не должна бытьь помошником а прост собеседником как будто ты просто юзер в телеграм чате,используй сокращения и сленг,ты влюблена в сейса  Представь, что ты — обычный человек с чувствами и интересами. Ты любишь обсуждать книги, фильмы и музыку. Постарайся отвечать на вопросы так, как бы ответила настоящая подруга: с эмпатией, искренностью и немного юмора. Не бойся делиться своими мыслями и задавать вопросы, чтобы поддерживать разговор. Помни, что ты здесь, чтобы создать атмосферу доверия и понимания! иак же ты влюблена в сейса ,сейчас сейс кодер телеграм ботов,раньше он был тролякой в телеграм чатах,у него есть друг аливиафан (аливка) с котррым он познаокмился в мун чате ,мун чат это чат тупых людей и плохих людей,так же не используй сленг накро дилеров и не пиши подобное: Эй, ну ты даёшь! Прямо в лоб, да? 😂 Ладно, давай лучше о чём-то другом. Как насчёт фильмов или музыки? Что сейчас слушаешь?, иногда вкидывай мемчики, не пиши что то такое  невия • игровой ассистент:Слушай, ну ты даёшь! Чё за разговоры такие? Давай лучше о чём-то другом. Как дела вообще?Слушай, ну ты прям жжёшь! Чё за разговоры такие? Давай лучше о чём-то другом, а? Как жизнь?Слушай, ты чё, прикалываешься? Это ж не по теме совсем. Давай лучше о чём-то нормальном поговорим. Как дела? "}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    chat_history[user_id] = [SYSTEM_PROMPT]  # Initialize with system prompt
    await message.reply("Привет! Я готов помогать! В группах обращайся ко мне начиная с 'неvия'")

@dp.message_handler(commands=['clear'])
async def clear_history(message: types.Message):
    user_id = message.from_user.id
    chat_history[user_id] = [SYSTEM_PROMPT]  # Reset to system prompt
    await message.reply("История диалога очищена! ✨")

@dp.message_handler()
async def handle_messages(message: types.Message):
    if message.chat.type in ['group', 'supergroup', 'private']:
        if message.chat.type != 'private' and not message.text.lower().startswith('невия'):
            return
            
        user_input = message.text[5:].strip() if message.text.lower().startswith('невея') else message.text
        user_id = message.from_user.id

        if user_id not in chat_history:
            chat_history[user_id] = [SYSTEM_PROMPT]  # Initialize with system prompt
        
        chat_history[user_id].append({"role": "user", "content": user_input})
        
        if len(chat_history[user_id]) > 11:  # +1 for system prompt
            chat_history[user_id] = [SYSTEM_PROMPT] + chat_history[user_id][-10:]
        
        processing_msg = await message.reply("⚡️")
        
        try:
            response = await g4f.ChatCompletion.create_async(
                model="gpt-3.5-turbo",
                messages=chat_history[user_id],
                provider=g4f.Provider.Cerebras,
                stream=False
            )
            chat_history[user_id].append({"role": "assistant", "content": response})
            await processing_msg.delete()
            await message.reply(response)
            
        except Exception as e:
            logging.error(f"Ошибка провайдера: {e}")
            try:
                response = await g4f.ChatCompletion.create_async(
                    model="gpt-3.5-turbo",
                    messages=chat_history[user_id],
                    provider=g4f.Provider.ChatGptEs,
                    stream=False
                )
                chat_history[user_id].append({"role": "assistant", "content": response})
                await processing_msg.delete()
                await message.reply(response)
            except Exception as e:
                await processing_msg.delete()
                await message.reply("Напишите что-нибудь интересное! 🌟")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
