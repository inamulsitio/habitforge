# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: HabitForge
def update_habit(self, habit_id, updates):
    """Update a habit's fields, raising on missing records."""
    try:
        rec = self._fetch_one("habit", {"id": habit_id})
    except HabitNotFoundError as e:
        raise HabitNotFoundError(f"Habit '{habits_id}' not found") from e

    if "name" in updates and updates["name"] is None:
        del updates["name"]
    for field, value in updates.items():
        rec[field] = value

    self._save("habit", [rec])
