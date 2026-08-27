# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: HabitForge
import sys

def handle_keyboard_interrupt():
    """Graceful handling of KeyboardInterrupt in CLI entry points."""
    print("\n\nKeyboardInterrupt detected. Saving current state...")
    try:
        from habitforge.app import save_state
        save_state()
    except ImportError:
        pass
    print("Goodbye!")
    sys.exit(0)
