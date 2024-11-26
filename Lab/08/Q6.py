import numpy as np
arr1 = np.random.randint(1,15,(5,3))
arr2 = np.random.randint(1,6,(3,2))
print(arr1,"\n")
print(arr2,"\n")
print(np.dot(arr1,arr2))
