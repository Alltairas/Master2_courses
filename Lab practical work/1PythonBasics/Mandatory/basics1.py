# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:13:34 2023

@author: aras
"""
import numpy as np

def AskRadius():
    radius = float(input('Enter the radius of the circle: '))
    return radius

def CircleArea(radius):
    return np.pi * (radius ** 2)

# Call the functions
radius = AskRadius()
area = CircleArea(radius)

# Print the result
print(f'The area of the circle with radius {radius} is: {area}')
