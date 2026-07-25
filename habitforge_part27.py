# === Stage 27: Add monthly summary calculations ===
# Project: HabitForge
from datetime import date, timedelta

def monthly_summary(records):
    """Compute streaks and totals for each month in a year."""
    months = {}
    current = date.today().year, 1
    while True:
        m_name, d = current.month, current.day
        if (current.year, current.month) not in months:
            months[(current.year, current.month)] = {
                "streak": 0, "days_active": 0, "total_reminders": 0
            }
        entry = months[(current.year, current.month)]
        if d <= 31 and any(
            rec["date"] == date(current.year, m_name, d) for rec in records
        ):
            entry["days_active"] += 1
            if entry["streak"] > 0:
                entry["streak"] += 1
        else:
            entry["streak"] = 0
        if current.month == 12 and current.year >= date.today().year:
            break
        current = (current.year, current.month + 1)
    return months
