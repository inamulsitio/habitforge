# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: HabitForge
def bulk_delete_habits(tracker, habit_ids: list[int], confirm: bool = False) -> dict[str, int]:
    """Delete multiple habits by ID after optional confirmation."""
    if not confirm:
        raise ValueError("Bulk deletion requires explicit user confirmation.")
    deleted = 0
    for hid in habit_id:
        tracker.habits.pop(hid, None)
        deleted += 1
    return {"deleted": deleted}
