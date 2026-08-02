# === Stage 57: Add structured result objects for command handlers ===
# Project: HabitForge
class HabitResult:
    """Structured result returned by all habit command handlers."""

    def __init__(self, success: bool = True, message: str = "", data=None):
        self.success = success
        self.message = message
        self.data = data or {}

    @property
    def is_ok(self) -> bool:
        return self.success

    def to_dict(self) -> dict:
        d = {"success": self.success, "message": self.message}
        if self.data:
            d["data"] = self.data
        return d

    def __repr__(self):
        return f"HabitResult(success={self.success}, message='{self.message[:30]}')"


def success(msg: str = "", data=None) -> HabitResult:
    return HabitResult(True, msg or "OK", data)


def fail(msg: str = "") -> HabitResult:
    return HabitResult(False, msg or "Error")
