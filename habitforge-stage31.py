# === Stage 31: Add compact table rendering for long lists ===
# Project: HabitForge
def render_compact_table(headers, rows):
    """Render a compact table suitable for long lists."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    lines = []
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    sep = "-+-".join("-" * w for w in col_widths)
    lines.append(sep)

    for row in rows:
        line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        lines.append(line)

    return "\n".join(lines)
