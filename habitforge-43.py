# === Stage 43: Add CSV import for the primary record type ===
# Project: HabitForge
def load_from_csv(csv_path: str) -> dict[str, list[dict]]:
    """Import habits and logs from a CSV with columns: type,name,date,description."""
    import csv, os
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    habits = []
    logs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = {"type": row["type"].strip(), "name": row["name"], "date": row.get("date", "").strip()}
            if not entry["name"]:
                continue
            entry.setdefault("description", "")
            if entry["type"] == "habit":
                habits.append(entry)
            elif entry["type"] in ("log", "streak"):
                logs.append(entry)
    return {"habits": habits, "logs": logs}
