# === Stage 38: Add data integrity checks for broken references ===
# Project: HabitForge
def check_integrity(db):
    """Validate cross-references between habits, routines, and reminders."""
    errors = []
    for habit in db.habits:
        if habit.id not in db._habits:
            errors.append(f"Orphaned habit ID {habit.id}")
        for routine in db.routines:
            if routine.habit_id != habit.id:
                continue
            if routine.id not in db._routines:
                errors.append(f"Orphaned routine linked to habit {habit.id}")
            for reminder in db.reminders:
                if reminder.routine_id != routine.id:
                    continue
                if reminder.id not in db._reminders:
                    errors.append(f"Orphaned reminder linked to routine {routine.id}")
    if errors:
        raise ValueError("Broken references detected:\n  " + "\n  ".join(errors))
