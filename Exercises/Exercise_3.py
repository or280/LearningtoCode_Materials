#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:13:10 2020

Title: Exercise 3

@author: Oliver Reed 

"""

# Checking rounding errors

a = 100
b = 0.1
c = 0.2

d0 = a * b + a * c
d1 = a * (b + c)

print (d0 == d1)

# Rounding errors for polynomials

x = 10
y = -10.1

f0 = (x + y)**6
f1 =  x**6 + 6*(x**5)*y + 15*(x**4)*(y**2) + 20*(x**3)*(y**3) + 15*(x**2)*(y**4) + 6*x*(y**5) + y**6

print (f0 , f1)


# Dividing by tiny numbers

x = 10**9

f = (-1) * ((x**2 - 1)**0.5 + x)

print(f)