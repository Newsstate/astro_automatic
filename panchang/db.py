
import sqlite3
from datetime import date

def init_db():
    conn = sqlite3.connect("panchang.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS panchang (
            date TEXT PRIMARY KEY,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_panchang(date_str, data_json):
    conn = sqlite3.connect("panchang.db")
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO panchang (date, data) VALUES (?, ?)", (date_str, data_json))
    conn.commit()
    conn.close()

def get_panchang(date_str):
    conn = sqlite3.connect("panchang.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM panchang WHERE date = ?", (date_str,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
