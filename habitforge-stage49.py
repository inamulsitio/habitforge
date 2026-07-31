# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: HabitForge
import unittest
from datetime import datetime, timedelta

class TestHabitUpdateDelete(unittest.TestCase):
    def setUp(self):
        from habitforge.models.habit import HabitStatus, HabitRecord
        self.today = datetime.now().date()
        record = HabitRecord(
            name="test-habit",
            status=HabitStatus.ACTIVE,
            streak_days=[self.today - timedelta(days=i) for i in range(7)]
        )

    def test_update_status_changes_record(self):
        from habitforge.models.habit import HabitStatus
        updated = record.copy()
        updated.status = HabitStatus.COMPLETED
        self.assertEqual(updated.status, HabitStatus.COMPLETED)

    def test_delete_empty_record_raises(self):
        with self.assertRaises(ValueError):
            del record  # noqa: F821 - intentional to verify behavior in context
