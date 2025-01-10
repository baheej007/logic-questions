def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))