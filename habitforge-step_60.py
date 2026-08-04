# === Stage 60: Add saved views for frequently used filters ===
# Project: HabitForge
class SavedView:
    def __init__(self, name, columns=None, filters=None):
        self.name = name
        self.columns = columns or []
        self.filters = filters or {}
