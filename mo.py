class Math:
    def add(self, a, b, c=0):  # Simulated method overloading
        return a + b + c

m = Math()
print(m.add(2, 3))      # Uses 2 arguments
print(m.add(2, 3, 4))   # Uses 3 arguments
