def pascal_triangle(n):
    triangle = [[1]]
    for _ in range(n - 1):
        row = [1] + [triangle[-1][i] + triangle[-1][i + 1] for i in range(len(triangle[-1]) - 1)] + [1]
        triangle.append(row)
    return triangle

print(pascal_triangle(5))
