# === Stage 42: Add CSV export without external dependencies ===
# Project: HabitForge
def export_to_csv(tracker, filename="habits.csv"):
    """Export all tracked habits to a CSV file without external dependencies."""
    import csv
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['habit_name', 'created_at', 'last_completed', 'streak_count'])
        
        for habit in tracker.habits.values():
            writer.writerow([
                habit.name,
                habit.created_at,
                habit.last_completed,
                habit.streak_count
            ])
