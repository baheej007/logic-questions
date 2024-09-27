def longest_zero_sum_subarray(nums):
    sum_to_index = {}  # To store the sum and corresponding index
    max_len = 0        # To store the maximum length of subarray
    current_sum = 0    # To store the running sum

    for i, num in enumerate(nums):
        current_sum += num

        # If current_sum is 0, we found a subarray from the beginning
        if current_sum == 0:
            max_len = i + 1

        # If current_sum is seen before, subarray with sum 0 exists
        if current_sum in sum_to_index:
            max_len = max(max_len, i - sum_to_index[current_sum])
        else:
            # Store the first occurrence of current_sum
            sum_to_index[current_sum] = i

    return max_len

# Example usage
nums = [1, 2, -3, 3, 4, -7, 2, 1]
print(longest_zero_sum_subarray(nums))  # Output: 5
