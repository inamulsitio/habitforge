# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: HabitForge
def snapshot_state(record):
    """Return a compact before/after snapshot of a record's key state."""
    return {
        "id": record["id"],
        "before": {k: v for k, v in record.items() if k != "id"},
        "after": {k: v for k, v in record.items() if k != "id"},
    }
