# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: HabitForge
def sort_habits(habits, key=None):
    return sorted(
        habits,
        key=lambda h: (h.get('priority', 0), h.get('title', '').lower(), h.get('last_update', '')),
        reverse=(key == 'priority'),
    )

def filter_habit_by_priority(habits, priority):
    return [h for h in habits if h.get('priority') == priority]
