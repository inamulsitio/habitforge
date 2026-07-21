# === Stage 16: Add argparse support for the most common commands ===
# Project: HabitForge
import argparse

def main():
    parser = argparse.ArgumentParser(description="HabitForge CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # log habit
    p_log = subparsers.add_parser("log", help="Log a completed habit")
    p_log.add_argument("--habit", required=True, help="Name of the habit")
    p_log.add_argument("--time", default=None, help="Time of completion (HH:MM)")

    # view today's log
    p_today = subparsers.add_parser("today", help="View today's logged habits")

    # show streaks
    p_streak = subparsers.add_parser("streak", help="Show current streaks")

    # reflect on a habit
    p_reflect = subparsers.add_parser("reflect", help="Write a reflection for a habit")
    p_reflect.add_argument("--habit", required=True, help="Name of the habit to reflect on")

    args = parser.parse_args()

    if hasattr(args, "command"):
        cmd = args.command.lower()
        if cmd == "log":
            log_habit(args.habit, args.time)
        elif cmd == "today":
            print_todays_log()
        elif cmd == "streak":
            show_streaks()
        elif cmd == "reflect":
            reflect_on_habit(args.habit)

if __name__ == "__main__":
    main()
