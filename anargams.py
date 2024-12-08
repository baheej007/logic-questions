def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted versions of the strings
    return sorted(str1) == sorted(str2)

# Example usage:
print(is_anagram("Listen", "Silent"))  # Output: True
print(is_anagram("Hello", "Olelh"))   # Output: True
print(is_anagram("Test", "Best")
