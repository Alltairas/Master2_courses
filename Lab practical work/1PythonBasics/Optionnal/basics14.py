# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:34:30 2023

@author: aras
"""

my_dict = {'Jean': 19, 'Claire': 22, 'Mathew': 21, 'Pierre': 20}

def key_of_min_val(d):
    # Check if the dictionary is empty
    if not d:
        return None
    
    # Find the key associated with the minimum value
    min_key = min(d, key=d.get)
    return min_key

def key_of_max_val(d):
    # Check if the dictionary is empty
    if not d:
        return None
    
    # Find the key associated with the maximum value
    max_key = max(d, key=d.get)
    return max_key

min_key = key_of_min_val(my_dict)
max_key = key_of_max_val(my_dict)

print(f"Key associated with the minimum value: {min_key}")
print(f"Key associated with the maximum value: {max_key}")
