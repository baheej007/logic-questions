from collections import defaultdict

my_word = "Mississippi"

d1 = defaultdict(list)

for index, letter in enumerate(my_word):
    if letter == "i":
        d1[letter].append(index)

print(d1)
