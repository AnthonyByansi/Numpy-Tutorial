# Obtaning array elements.
"""

Accessing an array element is the same as using an array index.
An array element's index number can be used to access it.
NumPy arrays' indexes begin at 0, therefore the first element has index 0, while the second has index 1.

"""

import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 8])
print(arr[2]) # An Element with index 2 is acessed.

# Acessing elements in a multi-demensional array

# 2D Array
arr1 = np.array([[1,3,5,7], [2,4,6,8]])
print("The 1st element in the 2nd row is ", arr1[1, 0])

# 3D array
arr3 = np.array([[[1,3,4,5,7], [3,5,6,8]], [[2,4,5,7], [3,4,6,7,8]]])
print(arr3[1,1,1])