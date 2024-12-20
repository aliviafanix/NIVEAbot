

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
SYSTEM_PROMPT = {"role": "system", "content": " отвечай 12 словами в основном.ты characterAI который всегда отвечает на русскрм.представь , ты 19 летняя девушка м что бы ты ответила на :  "}

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
        if message.chat.type != 'private' and not message.text.lower().startswith('невия2'):
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
                model="gpt-4-o",
                messages=chat_history[user_id],
                provider=g4f.Provider.DarkAI
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
                    provider=g4f.Provider.DarkAI,
                    stream=False
                )
                chat_history[user_id].append({"role": "assistant", "content": response})
                await processing_msg.delete()
                await message.reply(response)
            except Exception as e:
                await processing_msg.delete()
                await message.reply("Напишите что-нибудь интересное! 🌟")
