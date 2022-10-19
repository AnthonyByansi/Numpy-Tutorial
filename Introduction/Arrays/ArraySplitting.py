# For splitting, we make use of the array_split() function

import numpy as np 

arr = np.array([2,3,4,5,6,7])
re_array = np.array_split(arr, 2)

print(re_array[0])
print(re_array[1])

# The the above example shows how to split an array into 2 parts

arr1 = np.array([1,3,5,7])
arr2 = np.array([2,4,6,8])

arr3 = np.stack((arr1, arr2), axis=1)
print(arr)

# splitting along rows, here we use hsplit() function

arr4 = np.array([1,2,3])
arr5 = np.array([23,33,45])

arrz = np.hsplit((arr4, arr5), axis= 1)

# splitting along columns, here we make use of vsplit() function

arr6 = np.vsplit((arr4, arr5), axis=1)
print(arrz)
print(arr6)

# spliting along height... here we use the dsplit() function

arr7 = np.dsplit((arr4, arr5))
print(arr7)

