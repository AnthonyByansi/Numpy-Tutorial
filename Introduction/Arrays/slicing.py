# Python's "slicing" function transfers elements from one index to another index.
"""
In this case, 
we pass slice rather than index by [start:end]
The action can alternatively be defined as follows  [start:end:step]

"""

import numpy as np
arr = np.array(1,2,3,5,6,8)
print(arr[0:4])
print(arr[2:])


# slice elements from the beginning to index 3 (not inclusive)
print(arr[:3])

#slice elements from index 2 to index 1 
print(arr[-2:1])



