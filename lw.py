def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("The quick brown fox jumps over the lazy dog"))