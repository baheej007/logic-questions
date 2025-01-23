def caesar_cipher(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

print(caesar_cipher("Hello, World!", 3))
