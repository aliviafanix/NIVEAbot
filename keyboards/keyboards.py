from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для команды start"""
    keyboard = InlineKeyboardMarkup()
    url_button1 = InlineKeyboardButton(text="ℹ️ my weekdays", url="https://t.me/rvh_ebator")
    url_button2 = InlineKeyboardButton(text="➕", url="https://t.me/nevie_cfbot?startgroup=start")
    keyboard.add(url_button1, url_button2)
    return keyboard

def get_menu_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для меню"""
    rate = InlineKeyboardButton("зарабаток", callback_data="rate")
    nick = InlineKeyboardButton("основы", callback_data="nick")
    pref = InlineKeyboardButton("развлечение", callback_data="pref")
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.row(rate, pref)
    keyboard.row(nick)
    return keyboard

def get_modules_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для модулей"""
    keyboard = InlineKeyboardMarkup(row_width=2)
    sys_btn = InlineKeyboardButton("Системные модули", callback_data="sys_modules")
    user_btn = InlineKeyboardButton("Пользовательские модули [скоро]", callback_data="user_modules")
    keyboard.add(sys_btn, user_btn)
    return keyboard

def get_mining_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для шахты"""
    keyboard = InlineKeyboardMarkup()
    mine_btn = InlineKeyboardButton("⛏ Копать", callback_data="mine_stones")
    keyboard.add(mine_btn)
    return keyboard

def get_module_info_keyboard(module_name: str, is_enabled: bool) -> InlineKeyboardMarkup:
    """Клавиатура для информации о модуле"""
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    if not is_enabled:
        enable_btn = InlineKeyboardButton("✅ Включить", callback_data=f"enable_{module_name}")
        keyboard.add(enable_btn)
    else:
        disable_btn = InlineKeyboardButton("❌ Выключить", callback_data=f"disable_{module_name}")
        keyboard.add(disable_btn)
    
    back_btn = InlineKeyboardButton("↩️ Назад", callback_data="back_to_modules")
    keyboard.add(back_btn)
    return keyboard

def get_back_keyboard(callback_data: str = "back_to_modules") -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой назад"""
    keyboard = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton("↩️ Назад", callback_data=callback_data)
    keyboard.add(back_btn)
    return keyboard 