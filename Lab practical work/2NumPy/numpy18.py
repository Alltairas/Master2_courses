# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:35:54 2023

@author: aras
"""

import numpy as np

# Create a random 3x3 array
random_arr = np.random.random_sample((3,3))

print('Random 3x3 array =\n',random_arr)


# Delete the second row (axis=0)
arr_deleted_row = np.delete(random_arr, 1, axis=0)

print("\nArray after deleting the second row:")
print(arr_deleted_row)

# Delete the second column (axis=1)
arr_deleted_column = np.delete(random_arr, 1, axis=1)

print("\nArray after deleting the second column:")
print(arr_deleted_column)
