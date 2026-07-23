# === Stage 22: Add favorite records and quick favorite listing ===
# Project: HabitForge
import json, os

def favorite_records():
    try:
        with open("favorites.json", "r") as f:
            favs = json.load(f)
    except FileNotFoundError:
        favs = {}
    return favs

def add_favorite(habit_id):
    favs = favorite_records()
    if habit_id not in favs:
        print(f"Favorite added for habit: {habit_id}")
    else:
        print("Habit already favorited.")
    return favs[habit_id]

def remove_favorite(habit_id):
    favs = favorite_records()
    if habit_id in favs:
        del favs[habit_id]
        with open("favorites.json", "w") as f:
            json.dump(favs, f)
        print(f"Favorite removed for habit: {habit_id}")

def list_favorites():
    favs = favorite_records()
    if not favs:
        print("No favorites yet.")
        return
    for habit_id, count in favs.items():
        print(f"{habit_id}: favorited {count} time(s).")
