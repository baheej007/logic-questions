def find_duplicates(nums):
    seen, duplicates = set(), set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 5, 4]))