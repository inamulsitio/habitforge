# === Stage 4: Implement create operations for the primary records ===
# Project: HabitForge
import sqlite3

conn = sqlite3.connect("habitforge.db")
cur = conn.cursor()

# Habits: name, category (health/mental/productivity), created_at
cur.execute(
    """CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        category TEXT DEFAULT 'productivity',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
)

# Streaks: habit_id, current_streak, longest_streak, last_done_date
cur.execute(
    """CREATE TABLE IF NOT EXISTS streaks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER NOT NULL REFERENCES habits(id),
        current_streak INTEGER DEFAULT 0,
        longest_streak INTEGER DEFAULT 0,
        last_done_date TEXT
    )"""
)

# Routines: name, schedule_pattern (daily/weekly+day-name), reminder_time
cur.execute(
    """CREATE TABLE IF NOT EXISTS routines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER REFERENCES habits(id),
        name TEXT NOT NULL,
        schedule_pattern TEXT DEFAULT 'daily',
        day_name TEXT DEFAULT '',
        reminder_time TEXT DEFAULT ''
    )"""
)

# Reflections: user_id, date, mood (1-5), note, habit_id
cur.execute(
    """CREATE TABLE IF NOT EXISTS reflections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER DEFAULT 1,
        date TEXT NOT NULL,
        mood INTEGER CHECK(mood BETWEEN 1 AND 5),
        note TEXT DEFAULT '',
        habit_id INTEGER REFERENCES habits(id)
    )"""
)

conn.commit()
