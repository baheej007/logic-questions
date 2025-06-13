import numpy as np

arr = np.array([[2,3], [1,2], [9,8]])

print(arr[...,0])
"""
[2 1 9]
"""
print(arr[...])

"""
[[2 3]
[1 2]
[9 8]]
"""
