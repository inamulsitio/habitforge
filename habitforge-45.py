# === Stage 45: Add restore from backup with validation ===
# Project: HabitForge
def restore_backup(src_path, dst_dir):
    """Restore HabitForge data from a backup file with validation."""
    import os, json
    if not os.path.isfile(src_path) or not src_path.endswith('.json'):
        raise ValueError(f"Invalid backup: {src_path}")
    try:
        with open(src_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        raise IOError(f"Failed to read backup JSON: {e}")
    if not isinstance(data, dict):
        raise ValueError("Backup must be a JSON object")
    required_keys = {'habs', 'streaks', 'logs'}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys in backup: {missing}")
    try:
        with open(dst_dir, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        raise IOError(f"Failed to write restored data: {e}")
