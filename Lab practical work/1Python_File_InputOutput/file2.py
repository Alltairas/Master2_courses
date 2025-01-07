# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:03:21 2023

@author: aras
"""
file_path = "occupations.csv"
List = []

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        n = int(input('Enter the number of lines you want to read: '))
        
        for x in range(n):
            line = f.readline()
            if not line:
                break  # Break if there are no more lines in the file
            List.append(line.strip())  # Append the line to the list

        for item in List:
            print(item)
        
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")

