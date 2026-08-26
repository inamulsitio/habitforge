# === Stage 72: Add Markdown report export ===
# Project: HabitForge
def export_markdown_report(self, filename="habits_report.md"):
    """Export a Markdown report of all habits, streaks, and progress."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# HabitForge Report\n\n")
        for habit in self.habits.values():
            f.write(f"## {habit.name}\n")
            f.write(f"- **Streak:** {habit.streak_days} days\n")
            f.write(f"- **Last completed:** {habit.last_completed.strftime('%Y-%m-%d') if habit.last_completed else 'Never'}\n")
            f.write(f"- **Total completions:** {habit.total_completions}\n")
            f.write(f"- **Notes:** {habit.notes}\n")
            f.write(f"- **Reflection:** {habit.reflections[-1] if habit.reflections else 'None'}\n")
            f.write(f"- **Next reminder:** {habit.next_reminder.strftime('%Y-%m-%d %H:%M') if habit.next_reminder else 'Not set'}\n")
            f.write(f"- **Routine:** {habit.routine}\n")
            f.write(f"- **Created:** {habit.created.strftime('%Y-%m-%d') if habit.created else 'Unknown'}\n\n")
        f.write("---\n")
        f.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
    print(f"Report exported to {filename}")
