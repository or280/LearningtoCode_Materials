#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:26:39 2020

Title: Exercise 7

@author: Oliver Reed
"""

import numpy as np


# Summing large arrays.

a = np.random.rand(10000000)
b = np.random.rand(10000000)

c = np.zeros(10000000)
print (c)

#for i in range(10000000):
#    c[i] = c[i] + a[i] + b[i]

c = a + b
print(c)


# Working with arrays/scores.

scores = np.array([58.0, 35.0, 24.0, 42, 7.8])

def percent_rank(raw):
    percentages = scores/0.6
    return np.sort(percentages)

def statistics(raw, exclude=False):
    if exclude == False:
        max = np.max(raw)
        min = np.min(raw)
        mean = np.mean(raw)
        stats = {max, min, mean}
        return stats
    else:
        sorted = np.sort(raw)
        max = np.max(sorted[1:4])
        min = np.min(sorted[1:4])
        mean = np.mean(sorted[1:4])
        stats = {max, min, mean}
        return stats
        
    
    
p = percent_rank(scores)
print (p)

s = statistics(scores)
print (s)

s = statistics(scores, True)
print (s)


# 2D slicing.

A = np.array([[4.0, 7.0, -2.43, 67.1],
             [-4.0, 64.0, 54.7, -3.33],
             [2.43, 23.2, 3.64, 4.11],
             [1.2, 2.5, -113.2, 323.22]])
print(A)


# Third Column.
c3 = A[:,2:3]
print(c3)

# First 2 rows.
r2 = A[0:2]
print(r2)

# Bottom right 2 * 2 section.
br = A[2:4,2:4]
print(br)

# Sum last column.
c4 = A[:,3:4]
sum = 0
for i in c4:
    sum+=i
    
print(sum)

# Transpose.

T = np.transpose(A)
print(T)

