# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:09:05 2023

@author: aras
"""
from collections import Counter

def find_max_occurrence(List):
    counter = Counter(List)
    MaxOccurrence_item = counter.most_common(1)[0][0]
    
    return MaxOccurrence_item

# Example set:
original_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
result = find_max_occurrence(original_list)

print(f'The item with the most occurrences is: {result}')