# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:47:41 2023

@author: aras
"""

code_to_execute = '''
def greetings(name):
    print(f"Hello, {name}!")

greetings("World")
'''

try:
    exec(code_to_execute)
except Exception as e:
    print(f"An error occurred: {e}")
