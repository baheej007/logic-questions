def sum_of_unique_elements(nums):
    unique_sum = 0
    frequency = {}
    
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    for num, count in frequency.items():
        if count == 1:
            unique_sum += num
    
    return unique_sum

# Example usage
print(sum_of_unique_elements([1, 2, 3, 2]))  # Output: 4 (1 + 3)
