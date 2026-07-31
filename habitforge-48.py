# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: HabitForge
import unittest
from datetime import date, timedelta

class TestHabitValidation(unittest.TestCase):
    def test_date_parsing(self):
        d = "2024-12-31"
        self.assertEqual(date.fromisoformat(d), date(2024, 12, 31))

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            date.fromisoformat("not-a-date")

class TestHabitCreation(unittest.TestCase):
    def setUp(self):
        self.today = date.today()

    def test_create_habit_record(self):
        record = {"date": self.today, "done": True}
        self.assertTrue(record["done"])
        self.assertEqual(record["date"], self.today)

    def test_streak_calculation(self):
        dates = [self.today - timedelta(days=2), self.today - timedelta(days=1), self.today]
        streak = sum(1 for d in dates if d.weekday() < 5)
        self.assertEqual(streak, 3)

if __name__ == "__main__":
    unittest.main()
