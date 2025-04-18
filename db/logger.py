# db/logger.py

import sqlite3
from datetime import datetime
import os

DB_PATH = os.getenv("DB_PATH", "./logs/usage_logs.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            provider TEXT,
            prompt TEXT,
            response TEXT,
            tokens_used INTEGER,
            cost_usd REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_usage(provider, prompt, response, tokens_used, cost_usd):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usage_logs (timestamp, provider, prompt, response, tokens_used, cost_usd)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.now().isoformat(), provider, prompt, response, tokens_used, cost_usd))
