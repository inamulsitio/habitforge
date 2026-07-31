# === Stage 51: Add unit tests for search and filter behavior ===
# Project: HabitForge
import pytest
from datetime import date, timedelta


def test_search_by_name():
    habit = Habit(name="Exercise", streak=5)
    assert search_habits([habit], "Exerc") == [habit]
    assert search_habits([habit], "Sleep") == []


def test_filter_by_minimum_streak():
    h1 = Habit(name="Run", streak=7)
    h2 = Habit(name="Read", streak=3)
    filtered = filter_habits([h1, h2], min_streak=4)
    assert len(filtered) == 1
    assert filtered[0].name == "Run"


def test_filter_with_no_minimum():
    h = Habit(name="Meditate", streak=1)
    result = filter_habits([h], min_streak=None)
    assert result == [h]
