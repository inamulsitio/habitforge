# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: HabitForge
SETTINGS = {
    "reminder_time": "09:00",
    "notification_sound": "chime.wav",
    "reflection_prompt": "What did I learn today?",
    "weekly_goal": 5,
    "data_dir": "./habits_data",
}

def get_setting(key):
    """Return a setting value or the default if missing."""
    return SETTINGS.get(key)

def set_setting(key, value):
    """Update a single setting and print a confirmation message."""
    SETTINGS[key] = value
    print(f"Setting '{key}' updated to: {value}")
