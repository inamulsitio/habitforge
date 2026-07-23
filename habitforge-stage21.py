# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: HabitForge
def archive_records(db, older_than_days=30):
    today = datetime.now().date()
    cutoff = today - timedelta(days=older_than_days)
    archived_count = 0
    for record in db.records:
        if isinstance(record.created_at, date) and record.created_at < cutoff:
            record.archive_status = 'archived'
            archived_count += 1
    print(f"Archived {archived_count} old records.")

def restore_records(db, record_ids=None):
    if record_ids is None:
        record_ids = [r.id for r in db.records if r.archive_status == 'archived']
    restored_count = 0
    for rid in record_ids:
        rec = next((r for r in db.records if r.id == rid), None)
        if rec and rec.archive_status == 'archived':
            rec.archive_status = 'active'
            restored_count += 1
    print(f"Restored {restored_count} records.")
