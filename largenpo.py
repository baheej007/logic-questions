def find_second_largest(nums):
    if len(nums) < 2:
        return None

    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# Example usage:
numbers = [4, 1, 7, 3, 9, 7]
print(find_second_largest(numbers))  # Output: 7
