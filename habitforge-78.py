# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: HabitForge
def _parse_date_string(raw: str) -> datetime.date:
    """Parse common date formats into a date object."""
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.date.fromisoformat(raw)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {raw!r}")
