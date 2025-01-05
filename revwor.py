def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

print(reverse_words("Hello World"))