#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:34:40 2020

Title: Exercise 4

@author: Oliver Reed
"""

# Function to check if input is odd.

def is_odd(x):
    
    if x % 2 == 0:
        return False
    else:
        return True
    
print(is_odd(101))


# Function to find magnitude of a vector.

def magnitude(x,y,z = 0.0):
    
    mag = (x**2 + y**2 + z**2)**0.5
    return mag

print(magnitude(3,0,4))

# Function to find the area of a triangle given vertex co-ordinates.

def triangle_area(x0,y0,x1,y1,x2,y2):
    
    area = (x0*(y1 - y2) + x1*(y2 - y0) + x2*(y0 - y1))*0.5
    return abs(area)

print(triangle_area(0.0, 0.0, 0.0, 2.0, 3.0, 0.0))


# Function to find factorials using recursion.

import math
print("Reference factorial:", math.factorial(5))

def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of 5:", factorial(5))


# Function to perform the bisection evaluation method.

def f(x):
    return x**3 - 6*x**2 + 4*x + 12

def compute_root(f, x0, x1, tol, max_it):
    counter = 0
    error = 1.0
    while error > tol:
        x_mid = (x0 + x1)/2
        f0 = f(x0)
        f_mid = f(x_mid)
     
        if f_mid*f0 < 0:
            x1 = x_mid
        else:
            x0 = x_mid
        
        error = abs(x0 - x1)
        counter += 1

        # Guard against an infinite loop
        if counter > max_it:
            print("Oops, iteration count is very large. Breaking out of while loop.")
            break
    
    return x_mid, f(x_mid), counter

print(compute_root(f, x0=3, x1=6, tol=1.0e-6, max_it=1000))








