# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: HabitForge
class HabitScore:
    def __init__(self, habits):
        self.habits = {h.id: h for h in habits}

    def score_daily(self, date_str):
        scores = {}
        for h_id, habit in self.habits.items():
            streak = 0
            d = datetime.date.fromisoformat(date_str)
            if habit.last_completed and habit.last_completed.date() == d:
                streak += 1
            elif habit.last_completed and habit.last_completed.date() > d:
                continue
            else:
                for i in range(7):
                    day = (d - timedelta(days=i)).date()
                    if self.habits[h_id].last_completed and self.habits[h_id].last_completed.date() == day:
                        streak += 1
                    else:
                        break
            scores[h_id] = min(streak, 30) * habit.weight
        return sum(scores.values())

    def recommend(self):
        recs = []
        for h in self.habits.values():
            if h.streak < 5:
                recs.append((h.id, f"Increase {h.name} frequency or add reminders"))
            elif h.weight > 3 and h.completed_count < 10:
                recs.append((h.id, "Consider increasing habit weight or adding reflection prompts"))
        return recs[:5]

    def monthly_report(self):
        total = sum(h.completed_count for h in self.habits.values())
        total_possible = len(self.habits) * 30
        progress = (total / total_possible * 100) if total_possible > 0 else 0
        return {"completed": total, "progress_pct": round(progress, 1)}

    def display_dashboard(self):
        s = self.score_daily(datetime.date.today().isoformat())
        recs = self.recommend()
        report = self.monthly_report()
        print(f"Daily Score: {s}")
        print(f"Monthly Progress: {report['progress_pct']}%")
        print("Recommendations:")
        for h_id, msg in recs:
            habit = self.habits[h_id]
            print(f"- {habit.name}: {msg}")
