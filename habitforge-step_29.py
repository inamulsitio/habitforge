# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: HabitForge
def upcoming_reminders(reminders, days_ahead=7):
    """Return reminders sorted by due date within the next N days."""
    now = datetime.now()
    return sorted([r for r in reminders if (r["due"] - now).days <= days_ahead], key=lambda r: r["due"])

def get_reminder_types():
    """Return a list of reminder type names supported by HabitForge."""
    return ["daily", "weekly", "custom"]
