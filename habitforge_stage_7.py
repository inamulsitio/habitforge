# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: HabitForge
def format_streak(streak_count):
    if streak_count >= 30:
        return f"🔥 {streak_count} day streak!"
    elif streak_count >= 7:
        return f"👍 {streak_count} day streak"
    else:
        return f"🌱 {streak_count} day streak"

def format_routine_entry(entry):
    time_str = entry.get("time", "anytime")
    status = "✅ done" if entry.get("completed", False) else "⬜ pending"
    reminder = entry.get("reminder", "")
    reminder_part = f" | 🔔 {reminder}" if reminder else ""
    return f"{status} | {entry['name']} at {time_str}{reminder_part}"

def format_reflection(ref):
    mood = ref["mood"]
    emoji_map = {"great": "😄", "good": "🙂", "neutral": "😐", "bad": "😔", "terrible": "🤢"}
    return f"{emoji_map.get(mood, '❓')} | {ref['summary']}"

def format_daily_report(date_str, tasks, reflection):
    total = sum(1 for t in tasks if t["completed"])
    streak = next((t["streak"] for t in tasks if t["name"]), 0) or 0
    report = f"\n📅 {date_str}\n"
    report += "─" * 40 + "\n"
    for i, task in enumerate(tasks):
        line = format_routine_entry(task)
        report += f"{i+1}. {line}\n"
    if reflection:
        report += "\n📝 Reflection:"
        report += format_reflection(reflection) + "\n"
    else:
        report += "\n📝 No reflection today."
    return report

def print_welcome():
    banner = """
╔══════════════════════════╗
║  Welcome to HabitForge!  ║
║  Track habits, build     ║
║  streaks, reflect.       ║
╚══════════════════════════╝"""
    print(banner)

def format_progress_chart(tasks):
    if not tasks:
        return "\n📊 No progress chart yet."
    best = max(t["streak"] for t in tasks)
    bar_width = 20
    lines = ["📈 Progress Chart:\n", "─" * bar_width]
    for task in tasks:
        filled = int((task["streak"] / best) * bar_width) if best > 0 else bar_width
        line = f"{task['name'][:15]:>17} | {'█' * filled}{'░' * (bar_width - filled)} ({task['streak']} days)"
        lines.append(line)
    return "\n".join(lines)
