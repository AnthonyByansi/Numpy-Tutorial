# Python's core scientific computing library is called NumPy. Using a multidimensional array object is made possible by a Python package.

import numpy as np 
arr = np.array(['Owenn', "Lynatte","Tylor"])
print(arr)


#  1D array  
arr1 = np.array(["Joe", "Doe"])
print(arr1)
print("Dimension is ", arr1.ndim) 
print("size of the array is ", arr1.size) 
print("lenght of the array is  ", len(arr1))

# 2D Array 
arr2 = np.array([["Joe", "Doe"], ["John", "Conrad"]])
print(arr2)
print("Dimension is ", arr2.ndim) 
print("size of the array is ", arr2.size) 
print("lenght of the array is  ", len(arr2))

# 3D array 
arr3 = np.array([[["Ambrose", "Jason", "Nahiya"], ["Ambrose", "Jason", "Nahiya"]], [["Ambrose", "Jason", "Nahiya"], ["Ambrose", "Jason", "Nahiya"]]])
print(arr3)
print("Dimension is " , arr3.ndim)
print("The size of the array is ", arr3.size)
print("The length of the array is ",  len(arr3))
