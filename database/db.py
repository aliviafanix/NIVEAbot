import sqlite3
import json
from config.config import DB_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()
        self._create_tables()
        
    def _create_tables(self):
        # Таблица пользователей
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance INTEGER DEFAULT 0,
            mining_power INTEGER DEFAULT 1,
            last_mining TIMESTAMP
        )
        """)
        
        # Таблица модулей
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS modules (
            module_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            description TEXT,
            is_system BOOLEAN DEFAULT 0,
            is_enabled BOOLEAN DEFAULT 1,
            commands TEXT
        )
        """)
        
        # Таблица истории чата
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            response TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)
        
        self.conn.commit()
    
    def add_user(self, user_id: int, username: str):
        self.cur.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
                        (user_id, username))
        self.conn.commit()
    
    def get_user(self, user_id: int):
        self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return self.cur.fetchone()
    
    def update_balance(self, user_id: int, amount: int):
        self.cur.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?",
                        (amount, user_id))
        self.conn.commit()
    
    def get_balance(self, user_id: int) -> int:
        self.cur.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
        result = self.cur.fetchone()
        return result[0] if result else 0
    
    def update_mining_power(self, user_id: int, power: int):
        self.cur.execute("UPDATE users SET mining_power = ? WHERE user_id = ?",
                        (power, user_id))
        self.conn.commit()
    
    def update_last_mining(self, user_id: int):
        self.cur.execute("UPDATE users SET last_mining = CURRENT_TIMESTAMP WHERE user_id = ?",
                        (user_id,))
        self.conn.commit()
    
    def get_last_mining(self, user_id: int):
        self.cur.execute("SELECT last_mining FROM users WHERE user_id = ?", (user_id,))
        result = self.cur.fetchone()
        return result[0] if result else None
    
    def add_module(self, name: str, description: str, is_system: bool, commands: list):
        self.cur.execute("""
        INSERT INTO modules (name, description, is_system, commands)
        VALUES (?, ?, ?, ?)
        """, (name, description, is_system, json.dumps(commands)))
        self.conn.commit()
    
    def get_module(self, name: str):
        self.cur.execute("SELECT * FROM modules WHERE name = ?", (name,))
        return self.cur.fetchone()
    
    def get_all_modules(self, is_system: bool = None):
        if is_system is None:
            self.cur.execute("SELECT * FROM modules")
        else:
            self.cur.execute("SELECT * FROM modules WHERE is_system = ?", (is_system,))
        return self.cur.fetchall()
    
    def toggle_module(self, name: str, enabled: bool):
        self.cur.execute("UPDATE modules SET is_enabled = ? WHERE name = ?",
                        (enabled, name))
        self.conn.commit()
    
    def add_chat_message(self, user_id: int, message: str, response: str):
        self.cur.execute("""
        INSERT INTO chat_history (user_id, message, response)
        VALUES (?, ?, ?)
        """, (user_id, message, response))
        self.conn.commit()
    
    def get_chat_history(self, user_id: int, limit: int = 10):
        self.cur.execute("""
        SELECT message, response FROM chat_history
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
        """, (user_id, limit))
        return self.cur.fetchall()
    
    def clear_chat_history(self, user_id: int):
        self.cur.execute("DELETE FROM chat_history WHERE user_id = ?", (user_id,))
        self.conn.commit()

db = Database() 