# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:20:00 2023

@author: aras
"""

#Sample Dictionary: 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)

concatenated = {**dic1, **dic2, **dic3}

print(concatenated)
    