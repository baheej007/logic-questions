def find_subsets(lst):
    subsets = [[]]  # Start with an empty subset
    for num in lst:
        # For each number, add it to all existing subsets to create new subsets
        new_subsets = [subset + [num] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets

# Test input
lst = [1, 2]
print("Subsets:", find_subsets(lst))