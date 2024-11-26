import numpy as np
arr = np.random.choice([2,5,9,10], (4,4))
print(arr)
print((arr*np.eye(4))+np.array([1,3,5,7]))
