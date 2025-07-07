from collections import defaultdict

letters = defaultdict(int)

for letter in "Mississippi":
    letters[letter] += 1

print(letters)
