# === Stage 11: Add JSON export for the current application state ===
# Project: HabitForge
def export_state():
    """Export current application state to JSON."""
    import json, os
    state = {
        "habits": [h.to_dict() for h in habits],
        "routines": [r.to_dict() for r in routines],
        "reminders": [rm.to_dict() for rm in reminders],
        "reflections": reflections,
        "streaks": streaks,
    }
    with open("habits.json", "w") as f:
        json.dump(state, f, indent=2)
    print(f"State exported to habits.json ({len(habits)} habits, {len(routines)} routines)")
