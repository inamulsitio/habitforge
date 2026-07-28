# === Stage 41: Add plain text import for a simple line-based format ===
# Project: HabitForge
class PlainTextImport:
    """A simple line-based text format for importing/exporting habit data."""

    def __init__(self, header_line="HabitForge v1"):
        self.header = header_line
        self.lines = []

    def add(self, line):
        self.lines.append(line.strip())

    def to_text(self):
        result = [self.header] + self.lines
        return "\n".join(result)

    @classmethod
    def from_text(cls, text):
        obj = cls()
        for line in text.split("\n"):
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("HabitForge v1"):
                continue
            obj.lines.append(stripped)
        return obj

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, "r") as f:
            content = f.read()
        return cls.from_text(content)

    def to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.to_text())
