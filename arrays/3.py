# Use a single operation (no loops) to multiply every element of an array by 3.

# For example, if we had an array of [1,6,3], the output would be [3,18,9].

import numpy as np 
c = np.array([1, 2, 3, 4, 5])

def mult_three(array):
    new_array = []
    for num in array:
        num *= 3
        new_array.append(num)
    print(new_array)

mult_three(c)