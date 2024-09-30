def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

print(first_non_repeated("swiss"))  # Output: "w"
