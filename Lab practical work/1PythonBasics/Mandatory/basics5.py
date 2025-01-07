# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:36:06 2023

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

def stringList():
    string_list = []
    
    while True:
        user_input = input('enter a name( or N to finish):')
        
        if user_input == 'N'or user_input == 'n' :
            break
        try:
            string = str(user_input)
            string_list.append(string)
        except ValueError:
            print('Invalid input, Please enter a string.')
        
    return string_list

def Remove_first_item(arg):
    arg.pop(0)
    return arg


numbers = number_list()
numbers = Remove_first_item(numbers)

strings = stringList()
strings = Remove_first_item(strings)

print(numbers + strings)

