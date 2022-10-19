"""
filtering is Getting some elements out of an existing array and creating a new array out of them
  a boolean index list is a list of booleans corresponding to indexes in the array 
"""


import numpy as np

arr = np.array([1,3,4,5,2,6])
y = [True, True, False, True, False, True]

re_arr = arr[y]
print(re_arr)


# creating array that will return only values higher tham a certain number e.g 10

arr1 = np.array(2,4,8,10,12,14,16,18,20)
filter_arr1 = []

for element in arr1:
    if element > 10:
        filter_arr1.append('True')
    else:
        filter_arr1.append('False')

re_arr2 = arr1[filter_arr1]

print(filter_arr1)
print(re_arr2)

