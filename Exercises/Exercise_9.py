#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:23:17 2020

Title: Exercise 9

@author: Oliver Reed
"""

# Testing the fibonacci sequence generator.

def f(n): 
    "Compute the nth Fibonacci number using recursion"
    if n < 0:
        raise ValueError("n must be greater than or equal to zero")
    elif n == 0:
        return 0  
    elif n == 1:
        return 1  
    else:
        return f(n - 1) + f(n - 2)  
       
assert f(0) == 0
assert f(1) == 1
assert f(2) == 1
assert f(3) == 2
assert f(10) == 55
assert f(15) == 610


import pytest
with pytest.raises(ValueError):
    f(-1)
with pytest.raises(ValueError):
    f(-2)
    
print (f(10))
    

# Testing bisection algorithm.

def f(x):
    return x**3 - 6*x**2 + 4*x + 12

def compute_root(f, x0, x1, tol, max_it):
    counter = 0
    error = 1.0
    if tol < 0:
        raise ValueError("tolerance must be greater than or equal to zero")
    elif max_it < 0:
        raise ValueError("maximum iterations must be greater than or equal to zero")
    else:
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

        
            if counter > max_it:
                raise RuntimeError("maximum number of iterations reached")
    
    return x_mid, f(x_mid), counter

print(compute_root(f, x0=3, x1=6, tol=1.0e-6, max_it=20))

with pytest.raises(RuntimeError):
    x, f, num_it = compute_root(f, x0=3, x1=6, tol=1.0e-6, max_it=20)