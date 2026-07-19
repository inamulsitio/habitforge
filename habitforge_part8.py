# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: HabitForge
def filter_habits(habits, **kwargs):
    if 'status' in kwargs:
        habits = [h for h in habits if h.get('status') == kwargs['status']]
    if 'category' in kwargs:
        habits = [h for h in habits if h.get('category') == kwargs['category']]
    if 'owner' in kwargs:
        habits = [h for h in habits if h.get('owner') == kwargs['owner']]
    if 'tag' in kwargs:
        habits = [h for h in habits if any(kwargs['tag'] in t for t in h.get('tags', []))]
    return habits
