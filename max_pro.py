def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for num in nums[1:]:
        # Temporarily store the current max_product before updating
        temp_max_product = max_product

        # Update the maximum product by considering the current number
        max_product = max(num, num * max_product, num * min_product)
        # Update the minimum product by considering the current number
        min_product = min(num, num * temp_max_product, num * min_product)
        
        # Update the result with the maximum product found so far
        result = max(result, max_product)

    return result

# Example usage
nums = [2, 3, -2, 4]
print(max_product_subarray(nums))  # Output: 6
