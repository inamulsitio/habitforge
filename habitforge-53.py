# === Stage 53: Add command help text and usage examples ===
# Project: HabitForge
HELP_BLOCKS = {
    "habit": (
        "Usage: habit <add|list|complete|delete> [options]",
        "  add <name>                Add a new habit",
        "  list                      List all habits with current streaks",
        "  complete <name>           Mark a habit as done today",
        "  delete <name>             Remove a habit permanently"
    ),
    "routine": (
        "Usage: routine <add|list|start|stop>",
        "  add <name> [--days Mon-Fri] [--time HH:MM]  Create a named routine with schedule",
        "  list                      Show all active routines",
        "  start <name>              Begin the next scheduled run",
        "  stop <name>               Cancel and remove the routine"
    ),
    "reminder": (
        "Usage: reminder <add|list>",
        "  add [--at HH:MM] [--days Mon-Fri] <text>     Create a recurring reminder",
        "  list                                           Show all active reminders"
    ),
    "reflect": (
        "Usage: reflect [--day YYYY-MM-DD]",
        "  No arguments   Start an interactive reflection session for today",
        "  --day DATE     Reflect on a specific past date"
    ),
    "progress": (
        "Usage: progress [options]",
        "  [no args]      Show current week's habit completion chart",
        "  --week YYYY-Ww Show the named ISO week summary (e.g. --week 2025-W14)"
    ),
    "status": (
        "Usage: status",
        "  Shows overall progress: streaks, routines running, reminders active"
    )
}

USAGE_TEXT = "\n".join(f"{k.upper()}: {v[0]}" for k, v in HELP_BLOCKS.items()) + "\n\n" + USAGE_TEXT


def print_help():
    print("\nHabitForge Commands:\n")
    print(USAGE_TEXT)
    print("Type 'habit <add|list|complete|delete>' or any command above to get full help.\n")
