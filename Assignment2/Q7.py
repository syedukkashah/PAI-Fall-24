import numpy as np
arr = np.random.randint(0, 50, (5,10))
print(arr)
print("index of min value: ", np.argmin(arr))
print("index of max value: ", np.argmax(arr))