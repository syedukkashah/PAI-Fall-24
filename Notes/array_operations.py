import numpy as np
import array as arr
array = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(array)
print(array.reshape(5,5))
print(ranarr)
print(ranarr.max()) #returns max value of element
print(ranarr.argmax()) #returns index of max element
print(ranarr.min())
print(ranarr.argmin())
print(ranarr[1:5]) #prints index 1-5
#numpy arrays have broadcasting abilities (multiple indexes can be init to one value)
ranarr[0:5] = 100
print(ranarr)
newArr = ranarr[0:5] #this is called slicing
print(newArr)
newArr[:] = 99 #sliced array broadcasted to value of 99
print(newArr)
print(ranarr) #changed made to sliced array will also be implemented in original arr
print(array>4) #prints bool values for index>4
bool_arr = array>4 #can be init to another arr
print(bool_arr) #returns array that has true if element>4 & false if not
print(array[bool_arr]) #when conditional statement/bool arr is used like this it prints values that are > 4
print(array[array>2]) #prints all values in array > 2 in this case
x = 2
print(array[array>x])
array = np.arange(0,10)
print(array)
#arithmetic operations
print(array+array) #2 arrays can be added, (arr[i] = arr[i]+arr[i])
print(array*array) #arr[i] = arr[i]*arr[i]
print(array-array)#arr[i] = arr[i]-arr[i]
print(array.sum()) #prints sum of all elements
print(array.mean()) #mean of elements
print(array.max()) #max element
arr_2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr_2d)
#axis 0 refer to the cols
print(arr_2d.sum(axis = 0)) #returns arr with sum of elements down the cols
print(arr_2d.shape) #returns dimensions
print(arr_2d.sum(axis = 1)) # returns arr with sum of elements across each row
