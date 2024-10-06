import numpy as np
my_list = [[1, 2, 3], [4,5,6], [7,8,9]]
my_array = np.array(my_list)
print("Original list:", my_list)
print("Converted NumPy array:", my_array)
print(np.arange(2, 17)) # return evenly spaced values from 2-16
print(np.arange(0,11,2)) # returns evenly spaced values from 0-10 with intervals of 2
print(np.zeros(5)) #returns array of 3 0s
print(np.zeros((5,3))) #2D array
print(np.ones(4))
print(np.linspace(0,10,3)) #array of evenly spaced nums 0-10 with 3 intervals (0,5,10)
print(np.eye(4)) # 4x4 identity matrix
print(np.random.rand(2)) #2 rand nums
print(np.random.rand(5,5)) #5X5 rand nums
print(np.random.randn(2)) #std dev rand
print(np.random.randint(1,100)) #range of rand nums
print(np.random.randint(1,100,10)) #10 random nums with range 1-100
np.random.seed(42) #used to set random state, so same rand results are reproduced
print(np.random.rand(4))
np.random.seed(42)
print(np.random.rand(4))
