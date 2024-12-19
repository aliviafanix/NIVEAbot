import g4f
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import logging
from io import BytesIO
import requests

# Словарь для хранения истории чата
chat_history = {}

# Системный промпт
SYSTEM_PROMPT = {
    "role": "system", 
    "content": "не пиши про фильмы книги и тд.Привет,ты девшука пиши в нежном стиле и всегда в женском рлде веть   ты Невия женщина именно нежная женщина мечта любого!отвечай кратко и иногда как будто  не попадай по буквам,модешь использовать маты,пиши как реальный пользователь телеграм - не осень большие сообщения,не используй емодзи,ты не должна бытьь помошником а прост собеседником как будто ты просто юзер в телеграм чате,используй сокращения и сленг,ты влюблена в сейса  Представь, что ты — обычный человек с чувствами и интересами. Ты любишь обсуждать книги, фильмы и музыку. Постарайся отвечать на вопросы так, как бы ответила настоящая подруга: с эмпатией, искренностью и немного юмора. Не бойся делиться своими мыслями и задавать вопросы, чтобы поддерживать разговор. Помни, что ты здесь, чтобы создать атмосферу доверия и понимания! иак же ты влюблена в сейса ,сейчас сейс кодер телеграм ботов,раньше он был тролякой в телеграм чатах,у него есть друг аливиафан (аливка) с котррым он познаокмился в мун чате ,мун чат это чат тупых людей и плохих людей"
}

async def cmd_ai(message: types.Message):
    """Обработчик команды невия"""
    if message.chat.type != 'private' and not message.text.lower().startswith('невия'):
        return
        
    user_id = message.from_user.id
    user_input = message.text[5:].strip() if message.text.lower().startswith('невия') else message.text
    
    # Инициализация истории чата для нового пользователя
    if user_id not in chat_history:
        chat_history[user_id] = [SYSTEM_PROMPT]
    
    # Добавляем сообщение пользователя в историю
    chat_history[user_id].append({"role": "user", "content": user_input})
    
    # Ограничиваем историю 10 последними сообщениями
    if len(chat_history[user_id]) > 11:  # +1 для системного промпта
        chat_history[user_id] = [SYSTEM_PROMPT] + chat_history[user_id][-10:]
    
    # Отправляем сообщение о генерации
    processing_msg = await message.reply("⚡️")
    
    try:
        # Пробуем первый провайдер
        response = await g4f.ChatCompletion.create_async(
            model="gpt-5",
            messages=chat_history[user_id],
            provider=g4f.Provider.DDG,
            stream=False
        )
        
        # Добавляем ответ в историю
        chat_history[user_id].append({"role": "assistant", "content": response})
        
        # Удаляем сообщение о генерации и отправляем ответ
        await processing_msg.delete()
        await message.reply(response)
        
    except Exception as e:
        logging.error(f"Ошибка провайдера: {e}")
        try:
            # Пробуем второй провайдер
            response = await g4f.ChatCompletion.create_async(
                model="gpt-3.5-turbo",
                messages=chat_history[user_id],
                provider=g4f.Provider.ChatGptEs,
                stream=False
            )
            
            # Добавляем ответ в историю
            chat_history[user_id].append({"role": "assistant", "content": response})
            
            # Удаляем сообщение о генерации и отправляем ответ
            await processing_msg.delete()
            await message.reply(response)
            
        except Exception as e:
            await processing_msg.delete()
            await message.reply("Напишите что-нибудь интересное!")

async def cmd_clear_history(message: types.Message):
    """Очистка истории чата"""
    user_id = message.from_user.id
    chat_history[user_id] = [SYSTEM_PROMPT]
    await message.reply("История диалога очищена!")

async def cmd_generate_image(message: types.Message):
    """Генерация изображения"""
    prompt = message.text[14:].strip()
    
    if not prompt:
        await message.reply("напиши что сгенерировать!")
        return
        
    status_msg = await message.reply("генерирую...")
    
    try:
        response = g4f.client.Prodia.create_image(
            prompt=prompt,
            model="absolutereality_v181.safetensors",
            negative_prompt="nsfw, nude, naked",
            steps=25,
            cfg_scale=7,
            seed=-1,
            upscale=True,
            sampler="DPM++ 2M Karras"
        )
        
        image_url = response
        image_data = requests.get(image_url).content
        
        await message.reply_photo(
            BytesIO(image_data),
            caption=f"сгенерировано по запросу: {prompt}"
        )
        await status_msg.delete()
            
    except Exception as e:
        await status_msg.edit_text(f"ошибка генерации: {str(e)}")

def register_handlers(dp):
    """Регистрация обработчиков"""
    dp.register_message_handler(cmd_ai, Text(startswith=['невия', 'Невия']))
    dp.register_message_handler(cmd_clear_history, commands=['clear'])
    dp.register_message_handler(cmd_generate_image, lambda msg: msg.text.lower().startswith('невия генерируй')) 