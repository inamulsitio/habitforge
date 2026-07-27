# === Stage 35: Add active user switching and user-specific records ===
# Project: HabitForge
class UserStore:
    def __init__(self, db):
        self.db = db
        self._users = {}

    def add_user(self, name, email=None):
        user_id = len(self._users) + 1
        self._users[user_id] = {"name": name, "email": email or "", "joined_on": datetime.now().strftime("%Y-%m-%d")}
        return user_id

    def get_users(self):
        return list(self._users.values())

    def switch_user(self, user_id):
        if user_id not in self._users:
            raise ValueError(f"User {user_id} does not exist.")
        return {"current_user": self._users[user_id]}

    def get_active_user(self):
        return self._active_user

    def set_active_user(self, user_id):
        if user_id not in self._users:
            raise ValueError(f"User {user_id} does not exist.")
        self._active_user = user_id
