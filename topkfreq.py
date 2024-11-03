from collections import Counter

def top_k_frequent(nums, k):
    frequency = Counter(nums)
    return [item for item, count in frequency.most_common(k)]

# Example usage
print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
