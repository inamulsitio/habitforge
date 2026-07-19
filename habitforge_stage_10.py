# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: HabitForge
import re


def case_insensitive_search(text: str, query: str) -> bool:
    """Return True if `query` is found in `text` ignoring case."""
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return bool(pattern.search(text))
