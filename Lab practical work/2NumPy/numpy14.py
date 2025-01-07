# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:06:21 2023

@author: aras
"""

import numpy as np

# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 9, 6],
                   [7, 8, 5]])

# Find the index of the maximum element along axis=1 (along rows)
max_index_along_rows = np.argmax(arr_2d, axis=1)

# Find the index of the maximum element along axis=0 (along columns)
max_index_along_columns = np.argmax(arr_2d, axis=0)

print("Original 2D array:")
print(arr_2d)

print("\nIndex of the maximum element along rows:")
print(max_index_along_rows)

print("\nIndex of the maximum element along columns:")
print(max_index_along_columns)
