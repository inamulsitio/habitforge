# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: HabitForge
import json, datetime

class HabitForge:
    def __init__(self):
        self.habits = {}  # name -> { 'streak': int, 'history': list }
        self.routines = [] # [name, habits]
        self.reminders = []# [habit, time, msg]
        self.reflections = [] # [date, habit, text]

    def add_habit(self, name):
        if name not in self.habits:
            self.habits[name] = {'streak': 0, 'history': [], 'last_check': None}
        return self.habits[name]

    def log_done(self, habit_name, date=None):
        d = datetime.date.today() if date is None else date
        h = self.habits[habit_name]
        h['last_check'] = d
        if not h['history']:
            h['streak'] += 1
        elif h['history'][-1] == d:
            pass
        else:
            gap = (d - h['history'][-1]).days
            h['streak'] = max(0, h['streak'] + 1) if gap <= 1 else 0
        h['history'].append(d.isoformat())

    def add_reflection(self, habit_name, text):
        self.reflections.append((datetime.date.today().isoformat(), habit_name, text))
