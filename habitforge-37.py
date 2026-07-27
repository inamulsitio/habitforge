# === Stage 37: Add recommendations for the next useful action ===
# Project: HabitForge
def suggest_next_action(context):
    """Return a single actionable suggestion based on recent habits."""
    if not context.get('recent_habits'):
        return 'Start by logging one habit today.'
    top = max(context['recent_habits'], key=lambda h: h['streak'])
    return f'Keep up the streak of {top["name"]} — it\'s your strongest habit right now.'
