# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 01:04:21 2023

@author: aras
"""
import numpy as np

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def Prime_Sum(n):
    primes_sum = 0
    count_primes = 0
    current_number = 2
    
    while count_primes < n:
        if is_prime(current_number):
            primes_sum += current_number
            count_primes += 1
        current_number += 1
    
    return primes_sum

n = int(input('Enter a value: '))
primeSum = Prime_Sum(n)

print('The sum of the first', n, 'prime numbers is:', primeSum)
