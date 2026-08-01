# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: HabitForge
def get_streak_days(habits: list[dict]) -> dict[str, int]:
    """Return a mapping of habit name to current consecutive streak length."""
    now = datetime.now().date()
    today_key = (now.year, now.month, now.day)
    streaks: dict[str, int] = {}
    for h in habits:
        name = h["name"]
        history = sorted(h.get("history", []), key=lambda x: x[0])
        if not history or history[-1][0] != today_key:
            streaks[name] = 0
            continue
        streak = 1
        for i in range(len(history) - 2, -1, -1):
            day = history[i][0]
            expected = (day[0], day[1], day[2]) + (0, 0, 0)[:3]  # ensure tuple of 3 ints
            if expected != today_key:
                streak += 1
                today_key = expected
        streaks[name] = streak
    return streaks


def get_weekly_summary(habits: list[dict]) -> dict[str, list[int]]:
    """Return a mapping of habit name to completion counts for the last 7 days."""
    now = datetime.now().date()
    today_key = (now.year, now.month, now.day)
    weekly: dict[str, list[int]] = {}
    for h in habits:
        name = h["name"]
        history = sorted(h.get("history", []), key=lambda x: x[0])
        counts = [0] * 7
        current_week_start = today_key[:2] + (today_key[2] - today_key[2] % 7,)
        for day_tuple in history:
            if len(day_tuple) >= 3 and (day_tuple[0], day_tuple[1]) == current_week_start[:2]:
                idx = (today_key[2] - day_tuple[2]) % 7
                counts[idx] += 1
        weekly[name] = counts
    return weekly


def get_monthly_summary(habits: list[dict]) -> dict[str, list[int]]:
    """Return a mapping of habit name to completion counts for the last 30 days."""
    now = datetime.now().date()
    today_key = (now.year, now.month, now.day)
    monthly: dict[str, list[int]] = {}
    for h in habits:
        name = h["name"]
        history = sorted(h.get("history", []), key=lambda x: x[0])
        counts = [0] * 30
        current_month_start = today_key[:2] + (today_key[2] - today_key[2] % 30,)
        for day_tuple in history:
            if len(day_tuple) >= 3 and (day_tuple[0], day_tuple[1]) == current_month_start[:2]:
                idx = (today_key[2] - day_tuple[2]) % 30
                counts[idx] += 1
        monthly[name] = counts
    return monthly


def get_daily_progress(habits: list[dict], target_date: tuple[int, int, int]) -> dict[str, bool]:
    """Return a mapping of habit name to whether it was completed on the given date."""
    result: dict[str, bool] = {}
    for h in habits:
        history = sorted(h.get("history", []), key=lambda x: x[0])
        found = False
        for day_tuple in history:
            if len(day_tuple) >= 3 and (day_tuple[0], day_tuple[1], day_tuple[2]) == target_date:
                found = True
                break
        result[h["name"]] = found
    return result


def get_overall_progress(habits: list[dict]) -> dict[str, float]:
    """Return a mapping of habit name to overall completion percentage over its history."""
    progress: dict[str, float] = {}
    for h in habits:
        history = h.get("history", [])
        if not history:
            progress[h["name"]] = 0.0
            continue
        total_days = len(set((d[0], d[1]) for d in history))
        completed_days = sum(1 for d in set(history) if (d[0], d[1]) == (d[0], d[1]))
        progress[h["name"]] = round(completed_days / total_days * 100, 2) if total_days else 0.0
    return progress


def get_habit_count(habits: list[dict]) -> int:
    """Return the number of defined habits in the system."""
    return len(habits)


def get_daily_average_progress(habits: list[dict]) -> float:
    """Return the average daily progress percentage across all habits and days."""
    if not habits:
        return 0.0
    total = 0.0
    count = 0
    for h in habits:
        history = sorted(h.get("history", []), key=lambda x: x[0])
        unique_days = set((d[0], d[1]) for d in history)
        total += len(unique_days)
        count += len(history)
    return round(total / count * 100, 2) if count else 0.0


def get_habit_count(habits: list[dict]) -> int:
    """Return the number of defined habits in the system."""
    return len(habits)
