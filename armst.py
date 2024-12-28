def is_armstrong(num):
    n = len(str(num))
    return num == sum(int(digit) ** n for digit in str(num))

print(is_armstrong(153))