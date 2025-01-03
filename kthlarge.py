def kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

print(kth_largest([3, 2, 1, 5, 6, 4], 2))