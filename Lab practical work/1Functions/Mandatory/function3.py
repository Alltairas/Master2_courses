# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:11:49 2023

@author: aras
"""

Sample_List = [8, 2, 3, -1, 7]

def list_multiplier(l):
    if len(l) == 0:
        return 1  # Return 1 for an empty list
    s = l[0]
    for x in range(1, len(l)):
        s = s * l[x]
    return s

s = list_multiplier(Sample_List)
print('the multiplication of all the elements of the sample list is. ',s)