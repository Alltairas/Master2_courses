# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:53:15 2023

@author: aras
"""
value = int(input('enter a value: '))

def Sum(value):
    Summ = 0
    for x in range(value):
        Summ = Summ + (x**3)
    return Summ

S = Sum(value)
print(S)