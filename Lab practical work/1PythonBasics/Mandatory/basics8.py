# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 01:17:20 2023

@author: aras
"""
def enter_num_list():
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


def MinVal_of_list(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    # Initialize Min with the first element of the list
    Min = numbers[0]
    # Iterate through the list starting from the second element
    for x in range(1, len(numbers)):
        if Min > numbers[x]:
            Min = numbers[x]
    return Min

def MaxVal_of_list(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    # Initialize Max with the first element of the list
    Max = numbers[0]
    # Iterate through the list starting from the second element
    for x in range(1, len(numbers)):
        if Max < numbers[x]:
            Max = numbers[x]
    return Max

numbers = enter_num_list()
Min = MinVal_of_list(numbers)
Max = MaxVal_of_list(numbers)

print('The maximum and minimum values of the entered list of numbers are: ', Max, ';', Min)