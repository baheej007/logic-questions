def second_largest(nums):
    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

print(second_largest([12, 35, 1, 10, 34, 1]))

