def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
text = "Hello World"
print(count_vowels(text))  # Output: 3
