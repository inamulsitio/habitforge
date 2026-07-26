# === Stage 32: Add pagination helpers for long console output ===
# Project: HabitForge
def paginate(text, chunk_size=80):
    """Yield text in fixed-size chunks for console pagination."""
    while len(text) > chunk_size:
        yield text[:chunk_size]
        text = text[chunk_size:]
    if text:
        yield text


class Pager:
    def __init__(self, lines_per_screen=24):
        self.lines = []
        self.lines_per_screen = lines_per_screen

    def add(self, line):
        self.lines.append(str(line))

    def clear(self):
        self.lines.clear()

    def display(self):
        total = sum(len(l) for l in self.lines)
        if total == 0:
            return
        while len(self.lines) > self.lines_per_screen:
            print('\n'.join(self.lines[:self.lines_per_screen]))
            self.lines = self.lines[self.lines_per_screen:]

    def __call__(self, line):
        self.add(line)


def format_report(report_lines, pager=None):
    if pager is None:
        pager = Pager()
    for line in report_lines:
        pager(line)
    return pager.display()


class HabitLog:
    def __init__(self, habit_name='Habit'):
        self.habit_name = habit_name
        self.entries = []

    def log(self, date_str='', note='', streak=0):
        self.entries.append({'date': date_str or 'today', 'note': note, 'streak': streak})

    def report(self, pager=None):
        lines = [f'Habit: {self.habit_name}', f'Total entries: {len(self.entries)}']
        for e in sorted(self.entries, key=lambda x: x['date'], reverse=True):
            lines.append(f"  {e['date']} | Streak: {e['streak']} | Note: {e['note']}")
        return format_report(lines, pager)


def paginate_file(path, chunk=4096):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    for part in paginate(text, chunk_size=chunk):
        print(part)
