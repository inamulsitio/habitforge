# === Stage 67: Add a function that returns key project metrics ===
# Project: HabitForge
def get_project_metrics(db, user_id=None):
    """Return key HabitForge metrics for the given user (or all users)."""
    from datetime import datetime, timedelta

    today = datetime.now().date()
    start_date = today - timedelta(days=30)

    if user_id:
        records = db.query(Record).filter(Record.user_id == user_id, Record.date >= start_date).all()
        routines = db.query(Routine).filter(Routine.user_id == user_id).all()
    else:
        records = db.query(Record).filter(Record.date >= start_date).all()
        routines = db.query(Routine).all()

    total_records = len(records)
    total_routines = len(routines)
    avg_daily_records = total_records / max(30, (today - start_date).days)

    if records:
        total_streak = sum(
            1 for _ in records
            if (datetime.now().date() - datetime.fromtimestamp(_recorded_at).date()).days <= 3
        )
        avg_reflection_length = sum(len(r.reflection) for r in records if r.reflection) / max(1, len(records))
    else:
        total_streak = 0
        avg_reflection_length = 0

    return {
        "total_records": total_records,
        "total_routines": total_routines,
        "avg_daily_records": round(avg_daily_records, 2),
        "total_streak": total_streak,
        "avg_reflection_length": round(avg_reflection_length, 2),
    }
