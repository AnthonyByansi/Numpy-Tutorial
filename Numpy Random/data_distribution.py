"""
Data Distribution is a list of all possible values, and how often each value occurs.

Such lists are important when working with statistics and data science.

"""

from numpy import random
y = random.choice([5, 6,7,8], p=[0.2, 0.6, 0.1, 0.1], size=(50))

print(y)

