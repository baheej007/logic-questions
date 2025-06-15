PI = 3.14159

def add(a, b):
    return a + b

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

print("Module loaded!")  # Runs when you import this module
