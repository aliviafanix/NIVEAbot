from .ai import register_handlers as register_ai_handlers
from .economy import register_handlers as register_economy_handlers
from .games import register_handlers as register_games_handlers
from .mining import register_handlers as register_mining_handlers

def register_all_handlers(dp):
    """Регистрация всех обработчиков"""
    register_ai_handlers(dp)
    register_economy_handlers(dp)
    register_games_handlers(dp)
    register_mining_handlers(dp) 