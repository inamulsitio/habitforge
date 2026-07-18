# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: HabitForge
def delete_habit(habit_id: str, confirm_delete: bool = False) -> dict[str, Any]:
    """Delete a habit by ID with optional confirmation flag."""
    if not isinstance(confirm_delete, bool):
        raise TypeError("confirm_delete must be True or False")
    with open(HABIT_FILE, "r") as f:
        habits = json.load(f)
    for i, h in enumerate(habits):
        if h["id"] == habit_id:
            deleted = habits.pop(i)
            return {"success": True, "message": f"Deleted '{deleted['name']}'.", "habit": None}
    raise ValueError(f"Habit with id {habit_id} not found.")
