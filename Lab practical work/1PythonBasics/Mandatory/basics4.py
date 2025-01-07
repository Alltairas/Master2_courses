# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:26:20 2023

@author: aras
"""

def number_list():
    number_list = []
    
    while True:
        user_input = input('Enter a number (or N to finish): ')

        if user_input.upper() == 'N':
            break

        try:
            number = float(user_input)
            number_list.append(number)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    return number_list

# Example usage
numbers = number_list()
print('The first 4 entered numbers are:', numbers[0],'; ',numbers[1],'; ',numbers[2],'; ',numbers[3])
