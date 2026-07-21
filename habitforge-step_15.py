# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: HabitForge
def dispatch(text):
    """Parse a short text command and return (action, *args)."""
    parts = text.strip().split(maxsplit=3)
    cmd = parts[0].lower()
    rest = " ".join(parts[1:]) if len(parts) > 1 else ""

    dispatch_map = {
        "add": ("add", rest),
        "done": ("done", rest),
        "streak": ("streak", rest),
        "routine": ("routine", rest),
        "reflect": ("reflect", rest),
        "chart": ("chart", rest),
    }

    return dispatch_map.get(cmd, (cmd, rest))
