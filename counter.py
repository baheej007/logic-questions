def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

print(char_frequency("programming"))