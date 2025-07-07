from collections import defaultdict

def return_hello():
    return "Hello!"

d1 = defaultdict(return_hello)

d1[1]
d1[2]
d1[3]

print(d1)
