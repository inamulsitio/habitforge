# === Stage 18: Add an activity log with timestamps and action names ===
# Project: HabitForge
import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action_name, timestamp=None):
        if timestamp is None:
            timestamp = datetime.datetime.now()
        entry = {"action": action_name, "timestamp": timestamp}
        self.entries.append(entry)
        return entry

    def get_log(self):
        return sorted(self.entries, key=lambda e: e["timestamp"], reverse=True)

    def clear(self):
        self.entries.clear()
