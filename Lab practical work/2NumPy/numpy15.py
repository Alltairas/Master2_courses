# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:06:49 2023

@author: aras
"""

import numpy as np

# Create two 1-D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Use np.column_stack to stack the arrays as columns
result = np.column_stack((array1,array2))

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nResulting 2-D array:")
print(result)
