# cost_tracker.py

import sqlite3
from config import DB_PATH  # Set the DB_PATH in config file for SQLite storage

def log_cost(model, usage, task_type, score):
    """
    Log cost and token usage to SQLite (or BigQuery).
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS usage_logs (
                    model TEXT, 
                    task_type TEXT, 
                    tokens_used INT, 
                    score REAL)''')
    
    c.execute("INSERT INTO usage_logs (model, task_type, tokens_used, score) VALUES (?, ?, ?, ?)",
              (model, task_type, usage["total_tokens"], score))
    
    conn.commit()
    conn.close()
