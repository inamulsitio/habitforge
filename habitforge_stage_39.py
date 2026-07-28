# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: HabitForge
def repair_habitforge_data(db_path="habits.db"):
    """Compact self-repair routine for common data integrity issues."""
    import sqlite3, os
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Remove orphaned habit logs (habit_id not in habits table)
    cur.execute("""DELETE FROM habit_logs 
                   WHERE habit_id NOT IN (SELECT id FROM habits)""")
    print(f"Removed {cur.rowcount} orphaned habit logs")
    
    # Fix NULL end_date on completed routines
    cur.execute("UPDATE routines SET end_date = '2099-12-31' WHERE end_date IS NULL AND is_complete = 1")
    print(f"Patched {cur.rowcount} incomplete-ended routines")
    
    # Rebuild missing progress chart summary if habit_logs table has data but progress_summary is empty
    cur.execute("SELECT COUNT(*) FROM progress_summary LIMIT 1")
    if cur.fetchone()[0] == 0 and cur.execute("SELECT COUNT(*) FROM habit_logs").fetchone()[0] > 0:
        cur.execute("""INSERT INTO progress_summary (summary_date) 
                       SELECT MIN(date) FROM habit_logs""")
        print("Rebuilt initial progress summary row")
    
    conn.commit()
    conn.close()
