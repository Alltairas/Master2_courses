# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:29:53 2023

@author: aras
"""

import numpy as np

# Create a random 8x8x3 array
random_arr = np.random.random_sample((8,8,3))

print('Random 8x8x3 array:\n',random_arr)

# Extract a subarray of shape (3x3x2) from random_array
subarray = random_arr[3:,3:,:2]

print('\nExtracted subarray of shape (3x3x2): \n',subarray)