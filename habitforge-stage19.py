# === Stage 19: Add undo support for the last simple mutation ===
# Project: HabitForge
class HabitForge:
    def __init__(self):
        self.habits = {}
        self.routines = []
        self.reminders = []
        self.reflections = []
        self.charts = []
        self._undo_stack = []
        self._max_undo = 5

    @property
    def undo(self):
        return len(self._undo_stack) > 0

    def _snapshot(self, obj, key):
        import copy
        try:
            data = getattr(obj, key) if isinstance(getattr(type(obj), 'key', None), str) else (obj.habits if hasattr(obj, 'habits') and not key else obj)
            self._undo_stack.append(copy.deepcopy(data))
        except Exception:
            pass

    def add_habit(self, name):
        import copy
        snapshot = copy.deepcopy(self.habits)
        self._undo_stack.append(snapshot)
        if len(self._undo_stack) > self._max_undo:
            del self._undo_stack[0]
        self.habits[name] = {
            'name': name,
            'streak': 0,
            'completed_dates': [],
            'created': datetime.now().isoformat(),
            'logs': []
        }

    def complete_habit(self, habit_name):
        import copy
        snapshot = copy.deepcopy(self.habits)
        self._undo_stack.append(snapshot)
        if len(self._undo_stack) > self._max_undo:
            del self._undo_stack[0]
        if habit_name in self.habits and datetime.now().date() not in self.habits[habit_name]['completed_dates']:
            today = datetime.now().strftime('%Y-%m-%d')
            self.habits[habit_name]['streak'] += 1
            self.habits[habit_name]['completed_dates'].append(today)
        return True

    def undo_habit(self, habit_name):
        import copy
        if len(self._undo_stack) > 0:
            snapshot = self._undo_stack.pop()
            if isinstance(snapshot, dict):
                self.habits.update(snapshot)
