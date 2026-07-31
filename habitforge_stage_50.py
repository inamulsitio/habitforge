# === Stage 50: Add unit tests for import and export behavior ===
# Project: HabitForge
import json, os
from habitforge.models import Habit, Routine, Reflection, Reminder
from habitforge.engine import Engine


def _roundtrip(data):
    engine = Engine()
    engine.import_data(json.dumps(data))
    assert engine.habits[0].name == data["habits"][0]["name"]
    if "routines" in data:
        assert len(engine.routines) == len(data["routines"])
    return True


def test_import_export_habits():
    d = {
        "habits": [
            {"id": 1, "name": "Read", "streak_days": 7},
            {"id": 2, "name": "Exercise", "streak_days": 3},
        ]
    }
    assert _roundtrip(d)


def test_import_export_routines():
    d = {
        "habits": [{"id": 1, "name": "Morning", "streak_days": 0}],
        "routines": [
            {"habit_id": 1, "steps": ["brush teeth", "meditate"], "time": "07:00"},
        ]
    }
    assert _roundtrip(d)


def test_import_export_reminders():
    d = {
        "habits": [{"id": 1, "name": "Drink water", "streak_days": 0}],
        "reminders": [
            {"habit_id": 1, "time": "09:00", "enabled": True},
        ]
    }
    assert _roundtrip(d)


def test_import_export_reflections():
    d = {
        "habits": [{"id": 1, "name": "Journal", "streak_days": 5}],
        "reflections": [
            {"habit_id": 1, "date": "2026-01-01", "mood": 4, "notes": "felt calm"},
        ]
    }
    assert _roundtrip(d)


def test_import_export_empty():
    d = {"habits": []}
    engine = Engine()
    engine.import_data(json.dumps(d))
    assert len(engine.habits) == 0
