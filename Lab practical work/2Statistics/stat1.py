# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:45:22 2023

@author: aras
"""

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

#axis=1 : columns, axis=0 : rows, we interpret the second axis as columns
Max = np.argmax(arr, axis=1)
Min = np.argmin(arr, axis=1)
diff_col = Max-Min
print(diff_col)
# don't know where the problem is but th solution should be [6,6,6]
Max1 = np.argmax(arr, axis=0)
Min1 = np.argmin(arr, axis=0)
diff_row = Max1-Min1
print(diff_row)