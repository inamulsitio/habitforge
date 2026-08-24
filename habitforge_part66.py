# === Stage 66: Add export of a short status dashboard ===
# Project: HabitForge
def dashboard_summary(data):
    today = datetime.date.today()
    lines = []
    lines.append(f"📊 HabitForge Dashboard — {today.isoformat()}")
    lines.append("=" * 40)
    if data.get("streaks"):
        max_streak = max(s["streak"] for s in data["streaks"])
        lines.append(f"🔥 Longest Streak: {max_streak} days")
    if data.get("routines"):
        done = sum(1 for r in data["routines"] if r.get("completed", False))
        lines.append(f"✅ Routines Done Today: {done}/{len(data['routines'])}")
    if data.get("reminders"):
        lines.append(f"🔔 Reminders Active: {len([r for r in data['reminders'] if r['status'] == 'active'])}")
    if data.get("reflections"):
        recent = [r for r in data["reflections"] if r.get("date") == today.isoformat()]
        lines.append(f"💭 Reflections Today: {len(recent)}")
    if data.get("progress"):
        total = data["progress"]["completed"] + data["progress"]["skipped"]
        pct = int(data["progress"]["completed"] / total * 100) if total else 0
        lines.append(f"📈 Completion Rate: {pct}%")
    return "\n".join(lines)
