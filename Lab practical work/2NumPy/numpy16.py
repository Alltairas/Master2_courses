# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:08:36 2023

@author: aras
"""
import numpy as np

arr = np.array([[10, 20, 30,],
                [40, 50, 0],
                [0, 6, 0],
                [0, 0, 0] ])


mean_along_rows = np.mean(arr, axis=1)
mean_along_columns = np.mean(arr, axis =0)
transposed_array = np.transpose(arr)

print("original matrix=\n",arr)
print('mean along the columns: ',mean_along_columns)
print('mean along the rows: ',mean_along_rows)
print('transposed Matrix=\n',transposed_array)
