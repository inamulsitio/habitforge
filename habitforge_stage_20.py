# === Stage 20: Add duplicate detection for newly created records ===
# Project: HabitForge
def detect_duplicates(records, new_record):
    """Check if a new record duplicates any existing one by key fields."""
    key_fields = ['title', 'description']
    for r in records:
        if all(getattr(new_record, f) == getattr(r, f) for f in key_fields):
            return True
    return False
