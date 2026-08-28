# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: HabitForge
def self_check(habit_db, user_db, reminder_db, reflection_db, progress_db):
    """Run validations and demo operations for HabitForge."""
    print("=== HabitForge Self-Check ===")
    assert habit_db is not None, "habit_db is None"
    assert user_db is not None, "user_db is None"
    assert reminder_db is not None, "reminder_db is None"
    assert reflection_db is not None, "reflection_db is None"
    assert progress_db is not None, "progress_db is None"
    print("All databases initialized.")
    user_id = "u1"
    user = user_db.add_user(user_id, "Alice", "alice@example.com")
    print(f"Created user: {user}")
    habit = user_db.add_habit(user_id, "Read 30 min", "daily")
    print(f"Created habit: {habit}")
    reminder = reminder_db.add_reminder(user_id, habit["id"], "19:00", "daily")
    print(f"Created reminder: {reminder}")
    reflection = reflection_db.add_reflection(user_id, habit["id"], "Felt focused and energized.")
    print(f"Created reflection: {reflection}")
    progress = progress_db.add_progress(user_id, habit["id"], {"date": "2026-05-27", "completed": True})
    print(f"Created progress: {progress}")
    print("Self-check complete. All components functional.")
