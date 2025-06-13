def some_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

some_function(1, 2, 3,  a=4, b=5, c=6)

"""
Args: (1, 2, 3)
Kwargs: {'a': 4, 'b': 5, 'c': 6}
"""
