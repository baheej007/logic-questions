def find_duplicates(arr):
    duplicates = []
    for num in arr:
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]))  # Output: [2, 3]
