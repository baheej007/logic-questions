def decorater1(func):
    def wrapper(a, b):
        print("Loading...")
        result = func(a, b)
        print("Result:", result)
        print("finished")
        return result
    return wrapper
def decorater2(func):
    def wrapper(a, b):
        print("Loading...")
        result = func(a, b)
        print("Result:", result)
        print("finished")
        return result
    return wrapper   
def decorater3(func):
    def wrapper(a, b):
        print("Loading...")
        result = func(a, b)
        print("Result:", result)
        print("finished")
        return result
    return wrapper

@decorater1
def add(a, b):
    return a + b
@decorater2
def sub(a,b):
    return a-b
@decorater3
def mul(a,b):
    return a*b
    

print(add(4,6))
print(sub(4,6))
print(mul(4,6))
