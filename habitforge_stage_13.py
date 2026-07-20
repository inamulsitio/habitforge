# === Stage 13: Add file save support using a configurable path ===
# Project: HabitForge
import os, json

SAVE_PATH = getattr(self.config, 'save_path', './habits.json')

def _ensure_dir():
    d = os.path.dirname(SAVE_PATH)
    if d:
        os.makedirs(d, exist_ok=True)

def save_habits(data):
    """Persist habits to JSON at a configurable path."""
    _ensure_dir()
    with open(SAVE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
