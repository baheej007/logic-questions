def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Example usage
print(find_missing_number([3, 0, 1]))  # Output: 2
