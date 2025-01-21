def matrix_multiply(A, B):
    rows, cols, common = len(A), len(B[0]), len(B)
    result = [[sum(A[i][k] * B[k][j] for k in range(common)) for j in range(cols)] for i in range(rows)]
    return result

print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))