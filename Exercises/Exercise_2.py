#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:39:47 2020

Title: Exercise 2

@author: Oliver Reed
"""

# Prints grade based on score

score = 90

if score >= 82 and score <= 100:
    print ("Excellent")
elif score >= 76.5 and score < 82:
    print ("Very Good")
elif score >= 66 and score < 76.5:
    print ("Good")
elif score >= 45 and score < 66:
    print ("Need Improvement")
elif score >= 0 and score < 45:
    print ("What you messing at?")
else:
    print ("Error, value not in range")
    
    
# Iterative bisection method using for loop


# Initial end points
x0 = 3.0
x1 = 6.0

# Use 15 iterations
for n in range(15):
    # Compute midpoint
    x_mid = (x0 + x1)/2

    # Evaluate function at left end-point and at midpoint
    f0 = x0**3 - 6*x0**2 + 4*x0 + 12
    f = x_mid**3 - 6*x_mid**2 + 4*x_mid + 12
    
    if f*f0 < 0:
        x1 = x_mid
    else:
        x0 = x_mid

    print(n, x_mid, f)
    
    
# Iterative bisection method using the while loop


# Initial end points
x0 = 3.0
x1 = 6.0

tol = 1.0e-6
error = tol + 1.0

# Iterate until tolerance is met
counter = 0
while error > tol:
     x_mid = (x0 + x1)/2
     f0 = x0**3 - 6*x0**2 + 4*x0 + 12
     f = x_mid**3 - 6*x_mid**2 + 4*x_mid + 12
     
     if f*f0 < 0:
        x1 = x_mid
     else:
        x0 = x_mid
        
     error = abs(x0 - x1)
     counter += 1

     # Guard against an infinite loop
     if counter > 1000:
        print("Oops, iteration count is very large. Breaking out of while loop.")
        break
    
     print(counter, x_mid, error)
     
     
     
# Sine series using for loop

import math

# Value at which to approximate sine
x = 1.5*math.pi

# Initialise approximation of sine
approx_sin = 0.0

for n in range(15):
    term = ((-1)**n) * (x**(2*n+1)) / (math.factorial(2*n+1))
    approx_sin += term
    print (approx_sin)
    
    
error = abs(math.sin(1.5*math.pi) - approx_sin)

print("The error is:")
print(error)



# Sine series using while loop

import math

# Value at which to approximate sine
x = 1.5*math.pi

# Tolerance and initial error (this just needs to be larger than tol)
tol = 1.0e-8
error = tol + 1.0

# Intialise approximation of sine
approx_sin = 0.0

# Initialise counter
n = 0

# Loop until error satisfies tolerance, with a check to avoid an infinite loop
while error > tol and n < 1000:
    
    term = ((-1)**n) * (x**(2*n+1)) / (math.factorial(2*n+1))
    approx_sin += term
    error = abs(approx_sin - math.sin(1.5*math.pi))
    
    n += 1
    
print("The error is:")
print(error)

print("Number of terms in series:")
print(n)
