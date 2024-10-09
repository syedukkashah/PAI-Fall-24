import numpy as np
myarr = np.arange(2,19,2).reshape(3,3)
print(myarr)
resultant = myarr * np.eye(3)
print(resultant)
