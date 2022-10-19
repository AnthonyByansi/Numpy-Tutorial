"""
joning aray in numpy entails putting 2 or more arrays i the single array
N0TE:  in numpy we join aarrays using axes while in sql we join tables basing on keys

We ACHIEVE THIS by using concatenation() function, by passing in a sequence of arrays

"""
import numpy as np 
arr1 = np.array([2,4,5,6])
arr2 = np,array([3,5,7])

arr3 = np.concatenate((arr1, arr2))
print(arr3)


# joining 2-D arrays

arr4 = np.array([[1,3,4,5,6], [1,3,4,53,56]])
arr5 = np.array([[3,4,5,6], [5,6,3,5]]
arr6 = np.concatenate((arr4, arr5), axis=1)

print(arr6)
