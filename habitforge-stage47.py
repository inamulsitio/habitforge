# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: HabitForge
import sys
sys.path.insert(0, '..')
from habitforge import HabitForge
from datetime import date, timedelta

app = HabitForge()
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# 1. Create a daily habit with a reminder and a reflection goal
habit = app.create_habit(
    name="Morning Run",
    description="Run for at least 30 minutes before work.",
    streak_start=yesterday,        # user already did it yesterday
    reminders=[{"time": "7:00 AM", "message": "Time to lace up!"}],
)

# 2. Log a reflection after completing today's run
app.log_completion(
    habit_id=habit.id,
    date=today,
    notes="Felt great, completed the full 5K.",
    mood="energetic",
    energy_level=8,
)

# 3. Build a weekly routine that includes this habit and two more
routine = app.create_routine(
    name="Monday Warrior",
    habits=[habit],
    schedule={"days": ["Monday"]},
    reminders=[{"time": "6:50 AM", "message": "Get ready for Monday!"}],
)

# 4. Add a streak goal so the user knows when to celebrate
app.set_streak_goal(habit_id=habit.id, target_days=7)

# 5. Fetch progress and print a summary
progress = app.get_progress()
print(f"{'='*30}")
print("HabitForge Demo Scenario")
print(f"{'='*30}")
print(f"Habit: {habit.name}")
print(f"Streak: {progress['streak']} days (goal: 7)")
print(f"Completed today: {app.get_today_completion(habit.id)}")
print(f"Mood logged: {progress['last_mood']} | Energy: {progress['last_energy']}/10")
print(f"Routine 'Monday Warrior' active: {routine.active}")
