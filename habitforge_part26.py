# === Stage 26: Add weekly summary calculations ===
# Project: HabitForge
def weekly_summary(data):
    """Calculate weekly statistics from daily habit records."""
    if not data:
        return {"avg_completion": 0, "streaks_7d": 0, "best_day": None}
    
    days = sorted(set(d["date"] for d in data))
    week_days = [day for day in days if (day.weekday() % 7) < 5]
    
    total_records = len(data)
    completed_count = sum(1 for d in data if d.get("completed", False))
    avg_completion = (completed_count / total_records * 100) if total_records > 0 else 0
    
    consecutive_streaks = []
    current_streak = 0
    for day in week_days:
        date_str = day.strftime("%Y-%m-%d")
        day_data = [d for d in data if d["date"] == date_str]
        if day_data and any(d.get("completed", False) for d in day_data):
            current_streak += 1
        else:
            consecutive_streaks.append(current_streak)
            current_streak = 0
    consecutive_streaks.append(current_streak)
    
    best_day = max(week_days, key=lambda d: sum(1 for dd in data if dd["date"] == d.strftime("%Y-%m-%d") and dd.get("completed", False)))
    
    return {
        "avg_completion": round(avg_completion, 2),
        "streaks_7d": max(consecutive_streaks) if consecutive_streaks else 0,
        "best_day": best_day.strftime("%Y-%m-%d") if best_day else None
    }
