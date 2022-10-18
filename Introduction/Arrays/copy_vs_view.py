"""
A copy of an array is a new array, but a view is simply a view of the old array. This is the primary distinction between a copy and a view of an array.

The data is the property of the copy, and any modifications made to the copy will not impact the original array, and vice versa.


The original array does not belong to the view, so any modifications made to the original array will also effect the view. The view does not own the data.

"""

# copy 
import numpy as np

arr = np.array([2,4,6,8,10])
cpy = arr.copy()
arr[2] = 12

print(arr)
print(cpy)

# View 
arr1 = np.array([1,3,5,7,9])
vue = arr1.view()
vue[2] = 20

print(arr1)
print(vue)

