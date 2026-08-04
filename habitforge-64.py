# === Stage 64: Add validation for relationship references ===
# Project: HabitForge
import re


def _validate_relationship_ref(ref: str, entity_id: str) -> None:
    pattern = r'^[a-zA-Z0-9._-]+$'
    if not ref or len(ref) > 256:
        raise ValueError(f"Invalid relationship reference '{ref}'")
    if not re.match(pattern, ref):
        raise ValueError(
            f"Relationship reference '{ref}' contains invalid characters; "
            f"only letters, digits, '.', '_', '-' are allowed."
        )
    if ref.lower() == entity_id.lower():
        raise ValueError(
            f"Circular reference detected: 'habit' references itself by ID '{entity_id}'."
        )


def validate_relationships(habit_data):
    habit = habit_data.get("habit")
    routine = habit_data.get("routine") if habit else None
    reminder = habit_data.get("reminder") if habit and routine else None

    errors = []

    if not habit:
        return {"valid": False, "errors": ["Missing 'habit' data"]}

    _validate_relationship_ref(habit["id"], habit["id"])

    for field in ("title", "description"):
        val = habit.get(field)
        if not isinstance(val, str) or len(val.strip()) == 0:
            errors.append(f"Habit '{habit['id']}' has empty {field}.")

    if routine and not _validate_relationship_ref(routine["ref"], routine["ref"]):
        errors.append("Routine reference is invalid.")

    if reminder and not _validate_relationship_ref(reminder["ref"], reminder["ref"]):
        errors.append("Reminder reference is invalid.")

    return {"valid": len(errors) == 0, "errors": errors}
