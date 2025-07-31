import sqlite3

def init_db():
    conn = sqlite3.connect('mma.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        join_date TEXT,
        total_predictions INTEGER DEFAULT 0,
        correct_predictions INTEGER DEFAULT 0,
        points INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS fights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fighter1 TEXT,
        fighter2 TEXT,
        event_name TEXT,
        event_date TEXT,
        organization TEXT,
        status TEXT DEFAULT "upcoming",
        result TEXT,
        method TEXT,
        round INTEGER
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        fight_id INTEGER,
        predicted_winner TEXT,
        predicted_method TEXT,
        predicted_round INTEGER,
        is_correct INTEGER DEFAULT 0,
        points_earned INTEGER DEFAULT 0
    )''')
    conn.commit()
    conn.close()
