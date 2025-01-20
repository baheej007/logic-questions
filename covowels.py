def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    counts = {"vowels": 0, "consonants": 0}
    for char in s:
        if char.isalpha():
            if char in vowels:
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1
    return counts

print(count_vowels_consonants("Hello World"))
