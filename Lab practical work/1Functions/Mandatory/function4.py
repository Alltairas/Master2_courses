# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:18:21 2023

@author: aras
"""

def list_multiplier(l):
    if len(l) == 0:
        return 1  # Return 1 for an empty list
    s = l[0]
    for x in range(1, len(l)):
        s = s * l[x]
    return s

"""def factorial_of(n):
    List = [x + 1 for x in range(n)]  # Use list comprehension to create the list
    factorial = list_multiplier(List)
    return factorial"""
def factorial_of(n):
    List = []
    for x in range(n):
        List.append(x + 1)
    factorial = list_multiplier(List)
    return factorial

N = int(input('Enter the integer for which you want to compute the factorial: '))
f = factorial_of(N)
print(f'The factorial of {N} is {f}')

