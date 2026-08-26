# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: HabitForge
def seed_demo_data(db):
    """Populate a fresh HabitForge database with deterministic sample data."""
    from datetime import datetime, timedelta
    now = datetime.now()

    # Sample users
    users = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
    ]
    for name, email in users:
        db["users"].insert_one({
            "name": name,
            "email": email,
            "created_at": now - timedelta(days=30),
        })

    # Sample habits
    habits = [
        ("Meditate", "daily"),
        ("Read 30 minutes", "daily"),
        ("Exercise", "daily"),
        ("Drink 2L water", "daily"),
        ("Journal", "daily"),
        ("Code 1 hour", "daily"),
        ("Stretch", "every_other_day"),
        ("Review goals", "weekly"),
        ("Plan tomorrow", "daily"),
        ("Sleep 8 hours", "daily"),
    ]
    for name, frequency in habits:
        db["habits"].insert_one({
            "name": name,
            "frequency": frequency,
            "created_at": now - timedelta(days=60),
        })

    # Sample habit entries (last 14 days for streak visualization)
    for habit in habits[:4]:  # Just first 4 habits for demo
        for day_offset in range(14):
            entry_date = now - timedelta(days=14 - day_offset)
            db["entries"].insert_one({
                "habit_id": habit[0],
                "user_id": "Alice",
                "completed": day_offset % 3 != 0,  # Skip some days for variety
                "duration_minutes": 30 if habit[0] == "Read 30 minutes" else 25,
                "timestamp": entry_date,
            })

    # Sample routines
    routines = [
        ("Morning Routine", ["Meditate", "Exercise", "Journal"]),
        ("Evening Routine", ["Read 30 minutes", "Journal"]),
    ]
    for name, habit_list in routines:
        db["routines"].insert_one({
            "name": name,
            "habits": habit_list,
            "order": 1,
        })

    # Sample reflections
    reflections = [
        ("Felt great today, meditated for 20 minutes. Focused on breath.", "positive"),
        ("Skipped exercise, will do it tomorrow. Read for 45 minutes instead.", "neutral"),
        ("Completed all morning routine tasks. Felt energized.", "positive"),
    ]
    for text, sentiment in reflections:
        db["reflections"].insert_one({
            "text": text,
            "sentiment": sentiment,
            "created_at": now - timedelta(days=5),
        })

    print(f"Seeded {len(users)} users, {len(habits)} habits, 56 entries, {len(routines)} routines, {len(reflections)} reflections.")
