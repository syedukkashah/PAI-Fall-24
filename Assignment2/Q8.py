import numpy as np
A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 3]])
b = np.array([1, 2, 3])
solution = np.linalg.solve(A, b)
print("Array A: \n", A)
print("Array b:\n", b)
print("Solution (x, y, z):", solution)