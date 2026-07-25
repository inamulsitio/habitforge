# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: HabitForge
from datetime import date, timedelta


def parse_date(raw: str) -> date:
    """Parse a user-friendly date string into a ``date`` object."""
    raw = raw.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return date.fromisoformat(raw) if "%" not in fmt else __parse_fmt(fmt, raw)
        except ValueError:
            continue
    raise ValueError(
        f"Unrecognised date format '{raw}'. "
        "Accepted formats: YYYY-MM-DD, MM/DD/YYYY, DD.MM.YYYY, YYYY/MM/DD."
    )


def __parse_fmt(fmt: str, raw: str) -> date:
    import re
    parts = [int(p) for p in re.findall(r"\d+", raw)]
    if len(parts) != 3:
        raise ValueError(
            f"Expected exactly three numbers for format '{fmt}', "
            f"got {len(parts)} from input '{raw}'."
        )
    y, m, d = parts
    try:
        return date(y, int(m), int(d))
    except ValueError as exc:
        raise ValueError(
            f"Invalid calendar date for format '{fmt}': {raw}. "
            f"{exc}"
        ) from None


def today() -> date:
    """Return today's date."""
    return date.today()


def days_between(a: date, b: date) -> int:
    """Return the absolute number of days between two dates."""
    delta = (b - a).days if b >= a else (a - b).days
    return delta
