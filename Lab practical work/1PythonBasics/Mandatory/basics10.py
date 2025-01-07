# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:48:53 2023

@author: aras
"""

import random

Min = int(input('enter the Minima number of the list to be generated: '))
Max = int(input('enter the maxima number of the list to be generated: '))
n = int(input('enter the number of elements of the list to be generated: '))

# Generate a list of n random floats between Min and Max
def RandomlistGenerator(Min,Max,n):
    random_floats = [random.uniform(Min, Max) for _ in range(n)]
    return random_floats

def list_separator(List):
    separationPoint = int(input('enter the lenght of the first part'))
    firstpart = List[:separationPoint]
    secondpart = List[separationPoint:]
    return firstpart, secondpart

List = RandomlistGenerator(Min, Max, n)
Parts_of_list = list_separator(List)

print('first part: ', Parts_of_list[0])
print('second part: ', Parts_of_list[1])