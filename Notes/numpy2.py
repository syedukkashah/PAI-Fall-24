import numpy as np

def myAdd(x,y):
    return x+y


myAdd = np.frompyfunc(myAdd,2,1) #takes num of input arr & output arr
print(myAdd([1,2,3,4], [5,6,7,8]))
a = np.array([34,67,89,15,33,27])
string_generator = np.frompyfunc(str,1,1)
print(a)
print(string_generator(a))

arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
arr = np.array([1,1,1,2,3,4,5,5,6,7])
print(arr)
print(np.unique(arr))
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
print(np.setdiff1d(set1,set2)) #set subtraction(set1 - set2)
print(np.gcd(6,9)) #greatest common denominator
arr = np.array([20,8,32,36,16])
print(np.gcd.reduce(arr)) #GCD of arr
print(np.lcm(4,6)) #LCM
arr = np.arange(1,11)
print(np.lcm.reduce(arr)) #LCM of arr
arr = np.array([10,15,25,5])
print(arr)
print(np.diff(arr)) #subtracting two successive elements
print(np.diff(arr, n=2)) #[5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30
arr = np.array([1,2,3,4])
print(np.prod(arr)) #returns product of all elements (1*2*3*4)
arr2 = np.array([5,6,7,8])
print(np.prod([arr,arr2])) #prod of arr1*prod of arr2
print(np.add(arr,arr2)) #summation of sets
print(np.sum([arr,arr2])) #returns sum of both array elements
print(np.sum([arr,arr2], axis=1)) #returns row wise summation of both arrays
print(np.cumsum(arr)) # [1,1+2,1+2+3,1+2+3+4]
x = np.random.normal(loc=1, scale=2, size=(2, 3))
print(x)
x= np.random.binomial(n=10, p=0.5, size=10) #n = num of trials, p = probability of occurence of trial, size = shape of arr
print(x)
