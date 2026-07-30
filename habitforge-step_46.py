# === Stage 46: Add a schema version field and migration helper ===
# Project: HabitForge
SCHEMA_VERSION = 3


def migrate(schema):
    if schema.get("schema_version") != SCHEMA_VERSION:
        schema.setdefault("schema_version", SCHEMA_VERSION)
        schema["last_migrated"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        return True
    return False
