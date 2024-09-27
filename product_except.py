def product_except_self(nums):
    n = len(nums)
    
    # Create arrays to hold the product of elements to the left and right
    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n

    # Fill left_products array
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Fill right_products array
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Fill output array by multiplying left and right products
    for i in range(n):
        output[i] = left_products[i] * right_products[i]

    return output

# Example usage
nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))  # Output: [120, 60, 40, 30, 24]
