# === Stage 28: Add overdue item detection based on due dates ===
# Project: HabitForge
from datetime import date, timedelta


def _parse_date(s):
    """Parse a date string in YYYY-MM-DD or relative form."""
    if s.startswith(("today", "tomorrow")):
        return (date.today() + (timedelta(days=1) if s == "tomorrow" else timedelta(0))).isoformat()
    try:
        return date.fromisoformat(s).isoformat()
    except Exception:
        raise ValueError(f"Invalid date format: {s}")


def find_overdue_items(items, due_date_key="due_date"):
    """Return a list of items whose due_date is in the past (overdue)."""
    today = date.today().isoformat()
    overdue = []
    for item in items:
        if due_date_key not in item:
            continue
        try:
            due = _parse_date(item[due_date_key])
            if due < today and due != "":
                overdue.append({**item, **{"status": "overdue"}})
        except (ValueError, TypeError):
            pass
    return overdue


def mark_overdue(items, due_date_key="due_date", status_value="overdue"):
    """Update items with past due dates to a given status string in-place."""
    today = date.today().isoformat()
    for item in items:
        if due_date_key not in item or not isinstance(item[due_date_key], str):
            continue
        try:
            due = _parse_date(item[due_date_key])
            if due < today and due != "":
                item["status"] = status_value
        except (ValueError, TypeError):
            pass


# Example usage:
# items = [
#     {"title": "Read 30 min", "due_date": "2025-12-01"},   # overdue
#     {"title": "Exercise", "due_date": date.today().isoformat()},  # not overdue
# ]
# overdue = find_overdue_items(items)
