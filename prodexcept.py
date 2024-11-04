def product_except_self(nums):
    length = len(nums)
    answer = [1] * length
    
    prefix = 1
    for i in range(length):
        answer[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]
    
    return answer

# Example usage
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
