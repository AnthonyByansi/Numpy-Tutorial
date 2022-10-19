# for array searching, we use the where() meth9d.


import numpy as np
arr = np.array([1,2,3,2,5,6,2,6,2])
x = np.where(arr==2)
print(x) # here the output will be (array([1,3,6,8])) since value 2 is present at index 1 3 6 and 8

"""
SEARCH SORTED
here we use the searchsorted() which performs a binary search in the array

By default the left most index is returned, but we can give side='right' to return the right most index instead

"""

arrz = np.array([1,2,3,2,5,6,2,6,2])
y = np.searchsorted(arrz,3)
z = np.searchsorted(arrz,3, side= 'right')

print(y)
print(z)



