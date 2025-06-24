def decorator_function(original_function):
    def wrapper_function():
        print("Before original function")
        original_function()
        print("After original function")
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
