# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:18:32 2023

@author: aras
"""

import linecache

file_path = "occupations.csv"
n = int(input('Enter the line number you want to read: '))

try:
    line = linecache.getline(file_path, n)
    
    if not line:
        print(f"Error: Line {n} does not exist in the file.")
    else:
        print(line.strip())  # strip() removes the newline character

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except ValueError:
    print("Error: Please enter a valid line number.")
except Exception as e:
    print(f"An error occurred: {e}")