# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: HabitForge
def _resolve_imports(module):
    """Merge and deduplicate imports from multiple source files."""
    seen = set()
    merged = []
    for line in module.splitlines():
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from ') or stripped.startswith('#'):
            if stripped.startswith('#'):
                merged.append(line)
                continue
            key = stripped.replace('import ', '').replace('from ', '').replace(' as ', ' as ')
            if key not in seen:
                seen.add(key)
                merged.append(line)
    return '\n'.join(merged)
