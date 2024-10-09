import numpy as np
myArray = np.arange(1,19)
myArray = myArray[myArray%2!=0].reshape(3,3)
print(myArray)
