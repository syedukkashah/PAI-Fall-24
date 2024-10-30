import numpy as np
arr = np.arange(1,5).reshape(2,2)
print(arr)
print("determinant: \n", np.linalg.det(arr))
print("inverse: \n", np.linalg.inv(arr))