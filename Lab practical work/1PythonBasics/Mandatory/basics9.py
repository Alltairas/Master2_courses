# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:21:27 2023

@author: aras
"""

def remove_duplicates(numbers):
    duplicates_rmvd_numbers = []

    # Check if the list is empty
    if not numbers:
        return duplicates_rmvd_numbers

    for num in numbers:
        if num not in duplicates_rmvd_numbers:
            duplicates_rmvd_numbers.append(num)

    return duplicates_rmvd_numbers

# Example :
original_numbers = [1, 2, 2, 3, 4, 4, 5]
result_numbers = remove_duplicates(original_numbers)

print("Original list:", original_numbers)
print("List with duplicates removed:", result_numbers)
