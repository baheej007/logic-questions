def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

# Example
arr = [1, 2, 4, 5, 6]
n = 6
print(find_missing_number(arr, n))
