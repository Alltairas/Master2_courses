# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:59:13 2023

@author: aras
"""

import numpy as np

# Two example arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Stack the arrays horizontally to form a 2D array
data = np.column_stack((array1,array2))

# Calculate the Covariance Matrix
cov_matrix = np.cov(data,rowvar=True)

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nCovariance Matrix:")
print(cov_matrix)