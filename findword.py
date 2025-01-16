def find_subsets(s,w):
  subsets = [[]]  # Start with an empty subset
  for i in s:
      # For each number, add it to all existing subsets to create new subsets
      new_subsets = [subset + [i] for subset in subsets]
      subsets.extend(new_subsets)
  for w in subsets:

s = "ADOBECODEBANC"
w = "ABC"
print("Subsets:", find_subsets(s,w))
