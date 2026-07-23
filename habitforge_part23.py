# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: HabitForge
def tag_add(self, habit, tag):
    if habit.tag not in self.tags:
        self.tags[habit.tag] = []
    if habit not in self.tags[habit.tag]:
        self.tags[habit.tag].append(habit)
        return True
    return False

def tag_remove(self, habit, tag):
    if habit.tag == tag and len(self.tags[tag]) <= 1:
        del self.tags[tag]
    elif habit in self.tags.get(tag, []):
        self.tags[tag].remove(habit)
        return True
    return False

def tag_summary(self, tag=None):
    if tag is None:
        total = sum(len(v) for v in self.tags.values())
        return {"tagged": total}
    count = len(self.tags.get(tag, []))
    return {"tagged": count, "tags": {t: len(v) for t, v in self.tags.items()}}
