def find_subsets(s, w):
    subsets = [[]]
    result = []  # Store string representations of subsets
    
    for i in s:
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)
    
    for subset in subsets:
        k = "".join(subset)  # Convert subset list to a string
        result.append(k)
    
    return result  # Return all subset strings

s = "ADOBECODEBANC"
w = "ABC"
print("Subsets:", find_subsets(s, w))
