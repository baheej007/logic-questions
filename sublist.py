def find_subsets(s, w):
    subsets = [[]]
    result = []  # Store string representations of subsets
    valid_subsets = []  # Store subsets containing all characters of w

    # Generate all subsets
    for i in s:
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)

    # Convert subsets to strings
    for subset in subsets:
        k = "".join(subset)
        result.append(k)

    # Filter subsets that contain all characters of w
    for i in result:
        if all(i.count(char) >= w.count(char) for char in w):
            valid_subsets.append(i)

    return valid_subsets


s = "ADOBECODEBANC"
w = "ABC"
print("Subsets:", find_subsets(s, w))
