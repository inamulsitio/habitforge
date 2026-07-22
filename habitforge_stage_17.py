# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: HabitForge
def dry_run_mode():
    """Toggle a global flag so that any mutating command (add, remove, update) 
    writes to a temporary buffer instead of the real storage backend."""
    import json, os, tempfile
    
    def _dry_write(path, data):
        """Write `data` into an in-memory dict keyed by its filename, mimicking 
        the file-system write that production code would perform."""
        if not hasattr(dry_run_mode, '_store'):
            dry_run_mode._store = {}
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as tmp:
            json.dump(data, tmp)
            tmp.flush()
            dry_run_mode._store[path] = tmp.name
    
    def _dry_read(path):
        """Read the last in-memory write for `path`, or return an empty dict."""
        if not hasattr(dry_run_mode, '_store'):
            return {}
        return json.loads(open(_store.get(path), 'r').read()) if path in dry_run_mode._store else {}

    def _reset():
        """Discard all pending writes and reclaim the temporary files."""
        global _store
        if hasattr(dry_run_mode, '_store'):
            for tmp_path in _store.values():
                try: os.unlink(tmp_path)
                except OSError: pass
            _store = {}

    dry_run_mode._store = None
    return {
        'on': True,
        'write': lambda p, d: _dry_write(p, d),
        'read':  lambda p:  _dry_read(p),
        'reset': _reset,
    }
