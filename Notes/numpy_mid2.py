import numpy as np

#numpy function
#The frompyfunc() method takes the following arguments:
#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.

def myAdd(x,y):
    return x+y

myAdd = np.frompyfunc(myAdd,2,1)

#Implement a function that accepts a NumPy array and normalizes it (subtracts the mean and
#divides by the standard deviation). Apply this function to a sample array.

def normalize(arr):
    mean = arr.mean()
    std_dev = np.std(arr)
    return (arr - mean) / std_dev

print(np.arange(1,10))
print(np.array([1,2,3,4]))
print(np.ones(4))
print(np.zeros(4))
print(np.eye(4)) #identity mat
arr = np.array([1,4,2,94,18])
print(np.sort(arr))
print(np.linspace(0,10, 5))
print(np.random.rand(2)) #creates an array of given shape & populates it w/ random nums from 0-1
print(np.random.rand(3,2))
print(np.random.randn(3,3)) #std normal distribution
print(np.random.randint(1,100))
print(np.random.randint(1,100, (2,2)))
np.random.seed(55)
print(np.random.rand(4))
np.random.seed(55) #same seeds will print same set of rand nums
print(np.random.rand(4))
random_arr = np.random.randint(1,50,6) #(low,high,size) range is low to high-1
print(random_arr)
print(random_arr.max()) #max element
print(random_arr.min()) #min element
print(random_arr.argmax()) #max element index
print(random_arr.argmin()) #min element index
print(random_arr.sum()) #sums all elements
print(random_arr.mean()) #mean of array
arr = np.arange(1,11)
print(arr)
print(arr+arr)
print(arr-arr)
print(arr*arr)
print(arr/arr)

#axis = 0 is columns, axis = 1 is rows
arr_2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr_2d)
print(arr_2d.sum(axis=0)) #returns an array of size num columns of sum of column elements
print(arr_2d.sum(axis=1)) #does the same for rows

dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, #check how many dic rolls > 2
4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

print(dice_rolls[dice_rolls > 2].size)

#create numpy array called my_array which consists of 101 evenly spaced points b/w 0 & 10

my_array = np.linspace(0,10,101)
print(my_array)

#broadcasting
print(arr)
arr[0:5] = 100
print(arr)
arr_slice = arr[0:5]
arr_slice[:]=99
print(arr)

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print(np.linalg.inv(A)) #inverse of a matrix
print(np.linalg.det(A)) #determinant of a matrix
print(np.linalg.matrix_transpose(A)) #returns transpose of a matrix

#Create a one-dimensional NumPy array containing integers from 1 to 10. Compute the sum,
#mean, and product of the array
arr = np.arange(1,11)
print(arr.sum())
print(arr.mean())
print(arr.prod())

#Generate a 3x3 matrix with random integers. Calculate the transpose of the matrix.
arr = np.random.randint(1,11,(3,3))
print(arr)
print(np.linalg.matrix_transpose(arr))

#Create a NumPy array with 20 values and reshape it into a 4x5 matrix.
arr = np.arange(1,21).reshape(4,5)
print(arr)

#Perform element-wise addition, subtraction, multiplication, and division on two NumPy arrays
arr = np.arange(1,5)
arr2 = np.arange(5,9)
print(arr+arr,arr-arr2,arr*arr2,arr/arr2)

#Generate a 2x2 matrix and calculate its determinant and inverse.
arr = np.random.randint(1,10,(2,2))
print(arr)
print(np.linalg.det(arr))
print(np.linalg.inv(arr))

#Create a NumPy array with 50 random values. Find the indices of the maximum and minimum
#values in the array.

arr = np.random.randint(1,50,50)
print(arr)
print(arr.argmin())
print(arr.argmax())

#Create a 3x3 matrix representing a system of linear equations. Use NumPy to solve the system
#and print the solution.
A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 3]])
b = np.array([1, 2, 3])
print(np.linalg.solve(A,b))

#Create a NumPy array with 25 values and calculate the 75th percentile.
arr = np.arange(1,26)
print(np.percentile(arr,75))


print(normalize(arr))


print(myAdd([1,2,3,4], [5,6,7,8]))
