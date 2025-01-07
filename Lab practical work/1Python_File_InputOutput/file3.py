# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:26:45 2023
this code does the exercice 3 and 4 at the same time

@author: aras
"""
import random
import csv

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            line_count = sum(1 for _ in reader)
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "occupations.csv"
List1 = []
line_count = count_lines(file_path)

try:
    with open(file_path, 'r', encoding='utf-8') as f1:
        for _ in range(line_count):
            line = f1.readline()
            if not line:
                break  # Break if there are no more lines in the file
            List1.append(line.strip())  # Append the line to the list
        n = random.choice(List1)
        print('random line:', n)

except Exception as e:
    print(f"An error occurred: {e}")

try:
    List2 = []
    for _ in range(len(List1)):
        List2.append(random.choice(List1))
    
    with open('randomline.txt', 'w', encoding='utf-8') as f2:
        for line in List2:
            f2.write(line + '\n')  # Write each line to the file with a newline character

except Exception as e:
    print(f"An error occurred: {e}")