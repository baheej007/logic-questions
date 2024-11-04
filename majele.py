def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# Example usage
print(majority_element([3, 2, 3]))  # Output: 3
