# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: HabitForge
import json


def load_habit_json(filepath, default=None):
    """Load habit data from a JSON file with friendly error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        if default is not None:
            return default
        raise
    except json.JSONDecodeError as e:
        print(f"Warning: Malformed JSON in {filepath}: {e}")
        return [] if default is None else default
