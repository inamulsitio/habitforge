# === Stage 73: Add a lightweight HTML report export ===
# Project: HabitForge
import csv, datetime

class ReportExporter:
    def __init__(self, data):
        self.data = data

    def export_html(self, filename="habit_report.html"):
        today = datetime.date.today()
        streaks = sorted(self.data.get("streaks", {}).values(), key=lambda x: x["count"], reverse=True)
        routines = sorted(self.data.get("routines", {}).values(), key=lambda x: x["count"], reverse=True)
        reflections = self.data.get("reflections", [])[:5]
        streaks_html = "".join(f'<tr><td>{s["name"]}</td><td>{s["count"]}</td></tr>' for s in streaks[:10])
        routines_html = "".join(f'<tr><td>{r["name"]}</td><td>{r["count"]}</td></tr>' for r in routines[:10])
        reflections_html = "".join(
            f'<tr><td>{d["date"]}</td><td>{d["entry"]}</td></tr>' for d in reflections
        )
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>HabitForge Report</title>
<style>body{{font-family:sans-serif;margin:20px}}table{{border-collapse:collapse;width:100%%}}td{{border:1px solid #ccc;padding:8px}}th{{background:#f0f0f0}}</style></head>
<body><h1>HabitForge Progress Report</h1>
<p>Generated: {today}</p>
<h2>Top Streaks</h2><table><tr><th>Habit</th><th>Streak</th></tr>{streaks_html}</table>
<h2>Top Routines</h2><table><tr><th>Routine</th><th>Count</th></tr>{routines_html}</table>
<h2>Recent Reflections</h2><table><tr><th>Date</th><th>Entry</th></tr>{reflections_html}</table>
</body></html>"""
        with open(filename, "w") as f:
            f.write(html)
        return filename
