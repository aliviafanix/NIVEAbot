from typing import Union
from datetime import datetime
from ..config.config import DEVELOPER_IDS, ADMIN_IDS

def check_permissions(user_id: int) -> bool:
    """Проверка прав пользователя"""
    return user_id in ADMIN_IDS or user_id in DEVELOPER_IDS

def format_time(seconds: int) -> str:
    """Форматирование времени"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}ч {minutes}м {seconds}с"

def format_money(amount: Union[int, float]) -> str:
    """Форматирование денежных сумм"""
    return f"{amount:,}".replace(",", " ")

def get_current_timestamp() -> int:
    """Получение текущего timestamp"""
    return int(datetime.now().timestamp())

def parse_amount(text: str, max_amount: int = None) -> Union[int, None]:
    """Парсинг суммы из текста"""
    try:
        if text.lower() == "вб" and max_amount is not None:
            return max_amount
        amount = int(text)
        if amount < 0:
            return None
        if max_amount is not None and amount > max_amount:
            return None
        return amount
    except ValueError:
        return None 