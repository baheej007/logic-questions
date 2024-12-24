def most_frequent(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return max(frequency, key=frequency.get)

print(most_frequent([1, 3, 2, 3, 4, 3, 2, 1]))