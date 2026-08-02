# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: HabitForge
class Colored:
    """Tiny ANSI-colored printer for terminal output."""
    _RESET = "\033[0m"
    _RED = "\033[91m"
    _GREEN = "\033[92m"
    _YELLOW = "\033[93m"
    _BLUE = "\033[94m"
    _MAGENTA = "\033[95m"
    _CYAN = "\033[96m"

    @staticmethod
    def print_success(msg: str) -> None:
        if Colored._is_color():
            print(Colored._GREEN + msg + Colored._RESET)
        else:
            print(f"[OK] {msg}")

    @staticmethod
    def print_warning(msg: str) -> None:
        if Colored._is_color():
            print(Colored._YELLOW + msg + Colored._RESET)
        else:
            print(f"[WARN] {msg}")

    @staticmethod
    def print_error(msg: str) -> None:
        if Colored._is_color():
            print(Colored._RED + msg + Colored._RESET)
        else:
            print(f"[ERROR] {msg}")

    @staticmethod
    def print_info(msg: str) -> None:
        if Colored._is_color():
            print(Colored._BLUE + msg + Colored._RESET)
        else:
            print(f"[INFO] {msg}")

    @staticmethod
    def _is_color() -> bool:
        return getattr(__import__("sys"), "stdout").isatty() and os.environ.get("NO_COLOR") != "1"
