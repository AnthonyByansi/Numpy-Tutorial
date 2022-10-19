"""
stacking is the same as concatenation, however, stacking is done along a new axis

"""
import numpy as np
arr1 = np.array([1,3,5,7])
arr2 = np.array([2,4,6,8])

arr3 = np.stack((arr1, arr2), axis=1)
print(arr)

# stackimg along rows, here we use hstack() function

arr4 = np.array([1,2,3])
arr5 = np.array([23,33,45])

arrz = np.hstack((arr4, arr5), axis= 1)

# stacking along columns, here we make use of vstack() function

arr6 = np.vstack((arr4, arr5) axis=1)
print(arrz)
print(arr6)

# stacking along height... here we use the dstack() function
aarr4 = np.array([1,2,3])
arr5 = np.array([23,33,45])
