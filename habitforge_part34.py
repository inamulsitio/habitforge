# === Stage 34: Add support for multiple local user profiles ===
# Project: HabitForge
import json, os
from pathlib import Path

PROFILE_DIR = Path("profiles")

class UserProfiles:
    def __init__(self, data_file="users.json"):
        self.data_file = data_file
        PROFILE_DIR.mkdir(exist_ok=True)

    def _load(self):
        return json.loads(Path(self.data_file).read_text() or '{}')

    def save(self):
        Path(self.data_file).write_text(json.dumps(self._load(), indent=2))

    def register(self, username, email=None, display_name=None):
        profiles = self._load()
        if username in profiles:
            raise ValueError(f"Profile '{username}' already exists")
        profiles[username] = {
            "email": email or f"{username}@habitforge.local",
            "display_name": display_name or username,
            "streaks": {},
            "routines": [],
            "reminders": [],
            "reflections": []
        }
        self.save()

    def get_profile(self, username):
        return self._load().get(username)

    def list_profiles(self):
        return {u: p for u, p in self._load().items()}
