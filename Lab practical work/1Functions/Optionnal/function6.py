# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:07:42 2023

@author: aras
"""

def ask_integer():
    integer = int(input('Enter an integer: '))
    return integer

def prime_check(num):
    is_prime = True
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

num = ask_integer()
prime_check(num)