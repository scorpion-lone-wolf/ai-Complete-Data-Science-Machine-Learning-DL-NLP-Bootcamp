from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def cpu_heavy_task(n):
    for _ in range(n):
        pass
    return n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for i in numbers:
            future = executor.submit(cpu_heavy_task, (5000000))
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())
