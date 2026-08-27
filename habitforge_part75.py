# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: HabitForge
import os
import sys
from datetime import datetime, timedelta

def validate_habits(habits, routines, reminders, reflections, progress):
    warnings = []
    errors = []
    today = datetime.now().date()
    for habit in habits:
        if habit.get('created_at') is None:
            warnings.append(f"Habit '{habit.get('name', 'unnamed')}' has no creation date.")
        if habit.get('streak') is not None and not isinstance(habit['streak'], int):
            errors.append(f"Habit '{habit.get('name', 'unnamed')}' has non-integer streak value.")
        if habit.get('last_completed') is not None and habit['last_completed'] > today:
            warnings.append(f"Habit '{habit.get('name', 'unnamed')}' last_completed is in the future.")
        if habit.get('last_completed') is not None and habit['last_completed'] < today - timedelta(days=1):
            errors.append(f"Habit '{habit.get('name', 'unnamed')}' last_completed is over a day ago but streak is 0.")
    for routine in routines:
        if routine.get('schedule') is None:
            warnings.append(f"Routine '{routine.get('name', 'unnamed')}' has no schedule.")
        if routine.get('enabled') is False and routine.get('notes'):
            warnings.append(f"Disabled routine '{routine.get('name', 'unnamed')}' still has notes.")
    for reminder in reminders:
        if reminder.get('next_time') is None:
            warnings.append(f"Reminder '{reminder.get('name', 'unnamed')}' has no next_time.")
        if reminder.get('next_time') is not None and reminder['next_time'] < today:
            errors.append(f"Reminder '{reminder.get('name', 'unnamed')}' next_time is in the past.")
    for reflection in reflections:
        if reflection.get('mood') is not None and not isinstance(reflection['mood'], str):
            errors.append(f"Reflection has non-string mood value.")
        if reflection.get('duration') is not None and not isinstance(reflection['duration'], (int, float)):
            errors.append(f"Reflection has non-numeric duration value.")
    if not progress:
        warnings.append("Progress chart data is empty.")
    else:
        if len(progress) < 7:
            warnings.append("Progress chart has fewer than 7 data points for a week.")
    report = {"warnings": warnings, "errors": errors}
    return report
