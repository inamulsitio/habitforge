# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: HabitForge
def clear_state(self) -> bool:
    """Reset all trackers and return True if the user confirmed the reset."""
    if not self._confirm:
        return False
    self._streaks.clear()
    self._routines.clear()
    self._reminders.clear()
    self._reflections.clear()
    self._progress_data.clear()
    self._confirm = False
    return True
