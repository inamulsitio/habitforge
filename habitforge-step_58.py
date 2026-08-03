# === Stage 58: Add bulk update behavior for selected records ===
# Project: HabitForge
def bulk_update_records(db_path, record_id, field_name, value):
    """Bulk update a single field for all records in HabitForge database."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE habits SET {field_name} = ? WHERE id = ?", (value, record_id))
        conn.commit()
        updated_rows = cursor.rowcount
        print(f"Updated {updated_rows} row(s) for field '{field_name}' in record ID {record_id}.")
    except sqlite3.Error as e:
        print(f"Error updating records: {e}")
    finally:
        conn.close()

# Example usage:
bulk_update_records("habits.db", 1, "streak_count", 15)
