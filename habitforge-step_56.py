# === Stage 56: Add compact error classes for domain failures ===
# Project: HabitForge
class HabitError(Exception):
    """Base class for all HabitForge domain errors."""
    pass


class StreakBroken(HabitError):
    def __init__(self, expected: int, actual: int, habit_name: str) -> None:
        super().__init__(f"Habit '{habit_name}' streak broken: expected {expected}, got {actual}.")
        self.expected = expected
        self.actual = actual
        self.habit_name = habit_name


class ReminderMissed(HabitError):
    def __init__(self, scheduled_at: str) -> None:
        super().__init__(f"Reminder missed for scheduled time '{scheduled_at}'.")
        self.scheduled_at = scheduled_at


class ReflectionEmpty(HabitError):
    """Raised when a reflection entry is submitted without content."""

    pass


class ProgressCalculationFailed(HabitError):
    def __init__(self, reason: str) -> None:
        super().__init__(f"Progress calculation failed: {reason}")
        self.reason = reason


class RoutineConflict(HabitError):
    """Raised when a routine is scheduled at an overlapping time."""

    pass
