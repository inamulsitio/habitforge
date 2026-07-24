# === Stage 25: Add daily summary calculations ===
# Project: HabitForge
from datetime import date, timedelta


def daily_summary(habits: dict[str, list[dict]], user_id: str) -> dict:
    """Return a compact summary for today (and yesterday if needed)."""
    today = date.today()
    yesterday = today - timedelta(days=1)

    def _for_day(d):
        records = []
        streak = 0
        max_streak = 0
        current_run = set()
        for hname, logs in habits.items():
            day_logs = [l for l in logs if l["date"] == d]
            completed = [l for l in day_logs if l.get("completed", False)]
            skipped = [l for l in day_logs if not l.get("completed", False) and not l.get("skipped")]
            streak_today = 0
            consecutive = 0
            for log in sorted(day_logs, key=lambda x: x["timestamp"]):
                if log.get("status") == "done":
                    consecutive += 1
                elif log.get("status") == "missed":
                    current_run.clear()
                    consecutive = 0
                else:
                    continue
            # compute max consecutive done in this day's logs
            done_runs = []
            run_len = 0
            for l in sorted(day_logs, key=lambda x: x["timestamp"]):
                if l.get("status") == "done":
                    run_len += 1
                elif l.get("status") == "missed":
                    if run_len > 0:
                        done_runs.append(run_len)
                    run_len = 0
            max_run_today = max(done_runs + [run_len], default=0)

            records.append({
                "habit": hname,
                "completed": len(completed),
                "missed": len(skipped),
                "max_consecutive": max_run_today,
            })
        return {"date": d.isoformat(), "records": records}

    today_data = _for_day(today)
    yesterday_data = _for_day(yesterday)

    summary = {
        "user_id": user_id,
        "today": today_data if today_data["records"] else None,
        "yesterday": yesterday_data if yesterday_data["records"] else None,
    }
    return summary
