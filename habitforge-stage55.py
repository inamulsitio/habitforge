# === Stage 55: Add a setting to disable colorized output ===
# Project: HabitForge
import sys, os


def _is_color_enabled():
    return (os.environ.get("NO_COLOR", "").lower() == "true") and \
           (not hasattr(sys.stdout, "_color_forced"))


class _ColorDisabledOutput:
    """Redirect stdout/stderr if color is disabled."""

    def __init__(self):
        self._orig_stdout = sys.stdout
        self._orig_stderr = sys.stderr
        self._force_color = False
        try:
            import shutil
            self._term_supports_color = (shutil.get_terminal_size().columns > 0)
        except Exception:
            self._term_supports_color = True

    def set_force(self, enabled):
        if not hasattr(sys.stdout, "_color_forced"):
            sys.stdout._color_forced = enabled
        if not hasattr(sys.stderr, "_color_forced"):
            sys.stderr._color_forced = enabled


def _colorize(text, color_code=None):
    """Wrap *text* with ANSI escape codes for optional coloring."""
    if color_code and (os.environ.get("NO_COLOR", "").lower() != "true"):
        return f"\033[{color_code}m{text}\033[0m"
    return text


def print_habit_status(habit, day_name="Today", color=True):
    """Print today's habit status with optional color."""
    completed = (habit.completed and habit.streak > 0) or (
        hasattr(habit, "completed") and getattr(habit, "completed", False)
    )

    if not color:
        print(f"[{day_name}] Habit: {habit.name} | Status: {'Completed' if completed else 'Skipped'}")
    else:
        icon = "✅" if completed else "❌"
        status_text = f"{icon} {habit.name}" if completed else f"⏭️  {habit.name}"
        print(f"[{day_name}] Habit: {status_text}")


def log_progress_report(report_data, color=True):
    """Log a progress report with optional color highlighting."""
    total_habits = report_data.get("total", 0)
    completed_count = report_data.get("completed", 0)
    streak = report_data.get("current_streak", 0)
    best_streak = report_data.get("best_streak", 0)

    if not color:
        print(f"Progress: {completed_count}/{total_habits} habits done | Streak: {streak}/{best_streak}")
    else:
        bars = "█" * completed_count + "░" * (total_habits - completed_count)
        print(f"Progress:\n{bars}\nCompleted: {completed_count}/{total_habits} habits done")


def reflect_on_day(reflection_text, color=True):
    """Print a daily reflection with optional color."""
    if not color:
        print(f"\n=== Daily Reflection ===\n{reflection_text}")
    else:
        border = "=" * 50
        print(f"\n{border}")
        print(reflection_text)
        print(border)


def setup_color_mode(enable_color=True):
    """Configure whether color output is enabled."""
    if enable_color:
        os.environ.pop("NO_COLOR", None)
        try:
            import shutil
            term_cols = shutil.get_terminal_size().columns
            if term_cols > 0 and sys.stdout.isatty():
                print_habit_status({"name": "Test"}, color=True)
        except Exception:
            pass


def disable_color_output():
    """Disable all colorized output for HabitForge."""
    os.environ["NO_COLOR"] = "true"
    return True
