# === Stage 61: Add performance timing for core list and search operations ===
# Project: HabitForge
import time, random

def benchmark_list_ops():
    sizes = [100, 500, 2000]
    for n in sizes:
        data = list(range(n))
        t0 = time.perf_counter()
        _ = data + data[::-1] + sorted(data) + any(x % 3 == 0 for x in data) + all(x > 0 for x in data)
        elapsed = time.perf_counter() - t0 * 1e6
        print(f"List ops (n={n}): {elapsed:.2f} ms")

benchmark_list_ops()
