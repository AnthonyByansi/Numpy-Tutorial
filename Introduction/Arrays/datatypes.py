"""
The following are the few datatypes in numpy

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory

"""
import numpy as np
arr = np.array([[[1,3,4,5,7], [3,5,6,8]], [[2,4,5,7], [3,4,6,7,8]]])
print(arr.dtype) # datatype for the array object

#  creating array with defined datatype
arr2 = np.array([[[1,3,4,5,7], [3,5,6,8]], [[2,4,5,7], [3,4,6,7,8]]], dtype='i')
print(arr2.dtype)

# creating array with datatype 4 bytes interger
arr3 = np.array([[[1,3,4,5,7], [3,5,6,8]], [[2,4,5,7], [3,4,6,7,8]]], dtype='i4')
print(arr3.dtype)

# Converting Data Type on Existing Array
"""
The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

"""
arrz = np.array([2.5, 4.2, 2.4])
re_arrz = arrz.astype('i4')
print(re_arrz)
print(re_arrz.dtype)

arr3 = np.array([3.3, 4.4, 3.7])
re_arr3 = arrz.astype("b")
print(re_arr3)
print(re_arr3.dtype)