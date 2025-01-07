# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:29:05 2023

@author: aras
"""

def ask_integer():
    integer = int(input('Enter an integer: '))
    return integer

def create_list_between(a,b):
    l = []
    for x in range(a,b + 1):
        l.append(x)
    return l

def take_square(L):
    squared_list = [x**2 for x in L]
    return squared_list

i1 = ask_integer()
i2= ask_integer()
List =create_list_between(i1, i2)
squared_list = take_square(List)

print('original list: ',List)
print('squared list: ',squared_list)