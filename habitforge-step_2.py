# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: HabitForge
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional


@dataclass
class Habit:
    name: str
    description: str = ""
    streaks: dict[str, int] = field(default_factory=dict)  # habit_name -> current_streak

    def record_completion(self):
        today_str = date.today().isoformat()
        if self.streaks.get(today_str, 0) == self._calculate_streak():
            last_completed = max(date.fromisoformat(k) for k in self.streaks.keys()) if self.streaks else None
            yesterday_str = (last_completed - timedelta(days=1)).isoformat() if last_completed else today_str

        self.streaks[today_str] = 0


@dataclass
class Routine:
    name: str
    habits: list[str] = field(default_factory=list)

    def is_complete(self, completed_habits: set[str]) -> bool:
        return all(h in completed_habits for h in self.habits)


@dataclass
class Reflection:
    date: str  # ISO format
    mood: int  # 1-5 scale
    notes: str = ""
