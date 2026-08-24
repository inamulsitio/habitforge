# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: HabitForge
import datetime
import os

def reset_demo_data():
    """Reset all HabitForge data files to demo state for testing."""
    demo = {
        "habits": [
            {"id": "h1", "name": "Exercise", "category": "health", "frequency": "daily",
             "streak": 12, "total": 45, "created": "2023-01-01", "active": True},
            {"id": "h2", "name": "Read 30 min", "category": "learning", "frequency": "daily",
             "streak": 5, "total": 20, "created": "2023-02-15", "active": True},
            {"id": "h3", "name": "Meditate", "category": "mindfulness", "frequency": "daily",
             "streak": 30, "total": 90, "created": "2023-01-01", "active": True},
        ],
        "routines": [
            {"id": "r1", "name": "Morning Routine", "time": "07:00",
             "habits": ["h1", "h3"], "created": "2023-03-01"},
            {"id": "r2", "name": "Evening Routine", "time": "21:00",
             "habits": ["h2"], "created": "2023-03-01"},
        ],
        "reminders": [
            {"id": "rem1", "text": "Time to exercise!", "time": "07:30",
             "habits": ["h1"], "created": "2023-03-01"},
            {"id": "rem2", "text": "Read before bed", "time": "21:15",
             "habits": ["h2"], "created": "2023-03-01"},
        ],
        "reflections": [
            {"id": "ref1", "text": "Felt great after the workout!", "date": "2023-06-01",
             "habits": ["h1"], "rating": 5},
            {"id": "ref2", "text": "Book was engaging", "date": "2023-06-01",
             "habits": ["h2"], "rating": 4},
        ],
        "progress": [],
    }
    for fname in ["habits.json", "routines.json", "reminders.json",
                  "reflections.json", "progress.json"]:
        path = os.path.join("data", fname)
        if os.path.exists(path):
            with open(path, "w") as f:
                json.dump(demo.get(fname, []), f, indent=2)
        else:
            os.makedirs("data", exist_ok=True)
            with open(path, "w") as f:
                json.dump(demo.get(fname, []), f, indent=2)
    print("Demo data reset complete.")
