# Calculate the sum of an array of numbers. 
# Try doing this without using a loop 
# (refer to numpy's array methods to accomplish this).

# For example, if we had an array of [1,6,3], the output would be 10 (1+6+3=10).

import numpy as np
b = np.array([1,2,3,4])

def num_sum(array):
    print(array.sum())

num_sum(b)