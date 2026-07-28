# === Stage 40: Add plain text report export ===
# Project: HabitForge
def export_report(self, path="habitforge_report.txt"):
    """Export a plain text summary of all tracked data."""
    lines = [f"HabitForge Report: {self._name}", "=" * 60]
    for h in self.habits.values():
        if h["enabled"]:
            lines.append(f"\nHabit: {h['title']}")
            lines.append(f"  Streak: {h['streak']}, Last done: {h.get('last_done', 'Never')}")
            lines.append(f"  Done count: {len(h.get('history', []))}")
    if self.reminders:
        lines.append("\nReminders:")
        for r in self.reminders:
            lines.append(f"  - {r['name']} at {r['time']}")
    lines.append("\nDone.")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"Report saved to {path}")
