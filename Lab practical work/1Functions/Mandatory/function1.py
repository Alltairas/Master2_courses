# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:54:28 2023

@author: aras
"""
def wierd_request():
    int1 = int(input('enter an integer: '))
    Sum = 0
    for x in range(1,int1):
        Sum = x**3+ Sum 
    return int1, Sum

Sol = wierd_request()

print(f'the sum of cubes of all positive integers smaller than {Sol[0]} is {Sol[1]}')

""" the next exercice has already been done in the previous chapter with functions
"""
