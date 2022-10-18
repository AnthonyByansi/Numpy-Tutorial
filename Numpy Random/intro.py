# Pseudorandom numbers are those produced by a generating algorithm.

"""
Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

"""

from numpy import random
r = random.randint(50)
print(r)

# Random  float 
y  = random.rand()
x = random.rand(4) # this will generate a set of 4 random float

print(y)
print(x)