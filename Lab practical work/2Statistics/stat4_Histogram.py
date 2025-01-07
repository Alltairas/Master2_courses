# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:05:28 2023

@author: aras
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(1000)

# Create a histogram with 20 bins
plt.hist(data, bins=25, edgecolor='black')
plt.title('Histogram with 20 Bins')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Sample data
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])

# Specified bins
bins = np.array([0, 1, 2, 3])

# Compute the histogram
hist, bin_edges = np.histogram(nums, bins=bins)

print("nums:", nums)
print("bins:", bins)
print("Result:", (hist, bin_edges))