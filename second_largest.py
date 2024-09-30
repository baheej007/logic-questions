def second_largest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[-2] if len(unique_elements) >= 2 else None

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
