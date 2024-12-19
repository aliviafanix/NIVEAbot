import logging
from aiogram import Bot, Dispatcher, executor
from config.config import BOT_TOKEN
from database.db import db
from handlers import register_all_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def main():
    # Регистрация всех обработчиков
    register_all_handlers(dp)
    
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main() 