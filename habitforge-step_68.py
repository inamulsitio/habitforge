# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: HabitForge
def generate_changelog(self):
    """Build a compact changelog from the activity log."""
    lines = ["# HabitForge Changelog\n"]
    for entry in self.activity_log:
        lines.append(f"- **{entry['date']}**: {entry.get('note', '')}")
    return "\n".join(lines)
