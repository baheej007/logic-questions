def decorator(func):
    def wrapper(a, b):
        print("Loading...")
        result = func(a, b)
        print("Result:", result)
        print("finished")
        return result
    return wrapper

@decorator
def add_two_digits(a, b):
    return a + b

add_two_digits(4, 6)
