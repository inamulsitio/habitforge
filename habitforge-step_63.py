# === Stage 63: Add relationships between records where useful ===
# Project: HabitForge
import sqlite3


def add_relationships(db_path: str = "habits.db") -> None:
    """Add foreign key relationships between HabitForge tables."""

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Enable foreign keys for SQLite (must be explicit)
    cur.execute("PRAGMA foreign_keys = ON")

    # Users → Habits cascade delete, restrict update to same user_id
    try:
        cur.execute(
            "ALTER TABLE habits ADD CONSTRAINT fk_habits_user_id "
            "FOREIGN KEY(user_id) REFERENCES users(id) "
            "ON DELETE CASCADE ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass  # column may already be indexed

    # Users → Streaks cascade delete, restrict update to same user_id
    try:
        cur.execute(
            "ALTER TABLE streaks ADD CONSTRAINT fk_streaks_user_id "
            "FOREIGN KEY(user_id) REFERENCES users(id) "
            "ON DELETE CASCADE ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass

    # Users → Routines cascade delete, restrict update to same user_id
    try:
        cur.execute(
            "ALTER TABLE routines ADD CONSTRAINT fk_routines_user_id "
            "FOREIGN KEY(user_id) REFERENCES users(id) "
            "ON DELETE CASCADE ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass

    # Users → Reminders cascade delete, restrict update to same user_id
    try:
        cur.execute(
            "ALTER TABLE reminders ADD CONSTRAINT fk_reminders_user_id "
            "FOREIGN KEY(user_id) REFERENCES users(id) "
            "ON DELETE CASCADE ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass

    # Users → Reflections cascade delete, restrict update to same user_id
    try:
        cur.execute(
            "ALTER TABLE reflections ADD CONSTRAINT fk_reflections_user_id "
            "FOREIGN KEY(user_id) REFERENCES users(id) "
            "ON DELETE CASCADE ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass

    # Habits → Streaks restrict update to same habit_id
    try:
        cur.execute(
            "ALTER TABLE streaks ADD CONSTRAINT fk_streaks_habit_id "
            "FOREIGN KEY(habit_id) REFERENCES habits(id) "
            "ON DELETE RESTRICT ON UPDATE RESTRICT",
        )
    except sqlite3.OperationalError:
        pass

    conn.commit()
