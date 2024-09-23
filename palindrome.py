def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Example
number = 121
print(is_palindrome(number))  # True
