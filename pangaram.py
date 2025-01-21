def is_pangram(sentence):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))