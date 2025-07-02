import multiprocessing
import time

def is_prime(num):
    if num < 2:
        return None
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return None
    return num

if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    start_time = time.perf_counter()

    result = list(
        filter(
            lambda x: x is not None,
            pool.map(is_prime, range(0, 30))
        )
    )

    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time:.2f} seconds")
    print(result)
