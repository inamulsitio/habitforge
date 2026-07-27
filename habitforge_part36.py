# === Stage 36: Add templates for quickly creating common records ===
# Project: HabitForge
class RecordTemplate:
    """Templates for quickly creating common HabitForge records."""

    @staticmethod
    def daily_reflection():
        return {
            "type": "reflection",
            "title": f"Reflection for {datetime.date.today().isoformat()}",
            "date": datetime.date.today(),
            "content": "",
            "mood": None,
            "energy_level": None,
            "gratitude_notes": [],
            "lessons_learned": ""
        }

    @staticmethod
    def daily_routine():
        return {
            "type": "routine",
            "title": f"Routine for {datetime.date.today().isoformat()}",
            "date": datetime.date.today(),
            "activities": [],
            "completion_time": None,
            "notes": ""
        }

    @staticmethod
    def weekly_review():
        return {
            "type": "review",
            "title": f"Weekly Review: Week of {datetime.date.fromisocalendar(datetime.date.today().isocalendar()[1], datetime.date.today(), 1).strftime('%Y-%W')}",
            "date": datetime.date.today(),
            "summary": "",
            "achievements": [],
            "challenges_faced": [],
            "goals_adjustments": ""
        }

    @staticmethod
    def milestone_celebration():
        return {
            "type": "milestone",
            "title": f"Milestone: {datetime.date.today().isoformat()}",
            "date": datetime.date.today(),
            "achievement_description": "",
            "reflection_notes": ""
        }

    @staticmethod
    def habit_streak_update():
        return {
            "type": "streak_update",
            "title": f"Streak Update: {datetime.date.today().isoformat()}",
            "date": datetime.date.today(),
            "habit_name": "",
            "days_in_streak": 0,
            "notes": ""
        }
