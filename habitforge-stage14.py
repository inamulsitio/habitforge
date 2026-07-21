# === Stage 14: Add file load support with fallback demo data ===
# Project: HabitForge
def load_habits_data():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        demo = {
            "streaks": [7, 14, 3],
            "routines": ["Morning stretch", "Read 20 pages", "Meditate"],
            "reminders": [{"time": "8:00", "message": "Time to start your day!"}],
            "reflections": ["Felt great today", "Need more sleep"],
        }
        return demo
