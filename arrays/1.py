# Write a program that prints each item in a numerical array individually.
# imports numpy
import numpy as np
a = np.array([1,2,3,4])

def print_each(array):
    # just loop it and print each
    for num in array:
        print(num)

print_each(a)