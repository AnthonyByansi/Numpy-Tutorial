""""
Iterating entails going through each component one at a time.

Since numpy works with multi-dimensional arrays, we can accomplish this using the fundamental for loop in Python.

"""

# iterating through elements in a 1-D array 

import numpy as np 
arr1 = np.array([1,2,3,4,5])

for x in arr1:
    print(x)


# iterating through 2-D array
arr2 = np.array([[12,13,14,15],[17,26,27]])
for y in arr2:
    print(y)

# iterating through 3-D array
arr3 =  np.array([[[14,26,4564,3545],[12,23,35,67]], [[12,13,14,15],[17,26,27]]] )

for z in arr3: 
    print(z)

# to iterate down the scalars, we need to iterate arrays in each dimension

arrz = np.array([[[14,26,4564,3545],[12,23,35,67]], [[12,13,14,15],[17,26,27]]] )

for m in arrz:
    for n in m:
        for d in n:
            print(d)


# using thye nditer() function for iteration 
arr4 = np.array([[[14,26,4564,3545],[12,23,35,67]], [[12,13,14,15],[17,26,27]]] )

for g in np.nditer(arr4): # short and precise, isn't it?
    print(g)


# changing datatypes while iterating, here we make use of flag=['buffer']

arr5 = np.array([[[14,26,4564,3545],[12,23,35,67]], [[12,13,14,15],[17,26,27]]] )
for f in np.nditer(arr5, flags=['buffered'], op_dtypes=['S']):
    print(f)


"""
enumerated iteration using ndenumerate()

enumeration meand mentioning seqence number of things one by one 

"""

arr6 = np.array([[12,13,14,15],[17,26,27]])
for idk, k in np.ndenumerate(arr6):
    print(idk,k)


