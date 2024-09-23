def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example
arr = [10, 24, 45, 98, 23]
print(find_largest(arr))  # Output: 98
