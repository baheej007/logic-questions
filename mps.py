from math import floor, sqrt
import time

def is_prime(number: int) -> bool:
    if not (number & 1): return 0

    iteration = floor(sqrt(number)) + 1
    for i in range(3, iteration, 2):
        if not (number % i): return 0
    return 1

def prime_count_in_range(start: int, end: int) -> int:
    start_time = time.time()
    total = sum(is_prime(number) for number in range(start, end+1))
    end_time = time.time()
    print(f"Execution time is {end_time - start_time} where count of primes is {total} and start {start} end {end}")

    return total

def main() -> int:
    h_range = 10_000_000
    prime_count_in_range(1, h_range)

if __name__ == '__main__':
    main()
