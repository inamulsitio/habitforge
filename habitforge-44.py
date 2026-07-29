# === Stage 44: Add backup creation for the data file ===
# Project: HabitForge
def create_backup(data_file, backup_dir="./backups"):
    """Create a timestamped backup of the data file."""
    import os, shutil
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"habitforge_backup_{timestamp}.json")
    try:
        shutil.copy2(data_file, backup_path)
        print(f"[Backup] Saved to {backup_path}")
    except Exception as e:
        print(f"[Backup] Failed: {e}")
