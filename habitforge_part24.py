# === Stage 24: Add grouped summaries by category or status ===
# Project: HabitForge
def summarize_habits(habits, category_map=None):
    """Return a compact grouped summary of habits by status and optional category."""
    if category_map is None:
        category_map = {}
    groups = {}
    for h in habits:
        cat = category_map.get(h['category'], 'Other')
        key = (cat, h['status'])
        groups.setdefault(key, []).append({
            'name': h['name'],
            'streak': h['streak'],
            'last_done': h['last_done']
        })
    summary = []
    for (cat, status), items in sorted(groups.items()):
        avg_streak = sum(i['streak'] for i in items) / len(items) if items else 0
        last_dates = [i['last_done'] for i in items if i['last_done']]
        latest = max(last_dates) if last_dates else None
        summary.append({
            'category': cat,
            'status': status,
            'count': len(items),
            'avg_streak': round(avg_streak, 1),
            'latest_activity': latest
        })
    return summary
