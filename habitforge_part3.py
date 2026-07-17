# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: HabitForge
def validate_id(value):
    """Ensure a non-empty string identifier."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("ID must be a non-empty string.")
    return value.strip()

def validate_short_text(value, max_len=100):
    """Validate short free-text fields like titles and notes."""
    if not isinstance(value, str):
        raise TypeError(f"Expected str, got {type(value).__name__}")
    if len(value) > max_len:
        raise ValueError(f"text exceeds {max_len} characters.")
    return value

def validate_positive_number(value, allow_zero=False):
    """Accept integers and floats that are non-negative."""
    try:
        num = float(value)
    except (TypeError, ValueError):
        raise TypeError("number must be numeric")
    if not allow_zero and num < 0:
        raise ValueError("value must be >= 0")
    return num

def validate_bool(value):
    """Strict boolean check — reject truthy non-bools."""
    if value is not True and value is not False:
        raise TypeError(f"expected bool, got {type(value).__name__}")
    return bool(value)
