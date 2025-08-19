#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:56:49 2020

Title: Exercise 10

@author: Oliver Reed
"""

# ALgorithms giving max and min of a list.

import numpy as np

x = np.random.rand(1000)

def min_max1(x):
    x_min = 1.0
    x_max = 0.0
    for i in x:
        if i > x_max:
            x_max = i
    for i in x:
        if i < x_min:
            x_min = i
    return  x_min, x_max
    
print(min_max1(x))


def min_max2(x):
    x = np.sort(x)
    return x[0], x[len(x)-1]

print(min_max2(x))


# Function to implement Newtons root finding method.


def newton(f, df, x, tol=1e-8, max_it=20):
    counter = 0
    error = tol + 1.0
    while error > tol:
        error = abs(f(x)/df(x))
        x = x - f(x)/df(x)
        counter += 1
        print (x, counter, error)
        
        if counter > max_it:
                raise RuntimeError("maximum number of iterations reached")
    
    return  x, counter
    
    
def f(x):
    return np.tan(x) - 2*x
    
    
def df(x):
    dx = 1e-9
    dif = (f(x+dx) - f(x-dx))/(2*dx)
    return dif


print(newton(f,df, 0.2))



import matplotlib.pyplot as plt

x = np.linspace(-1.5, 1.5, 100)
plt.plot(x, f(x), label='$f(x)$')
plt.plot(x, df(x), label="$f^{\prime}(x)$")
#plt.show


# Low pass filter of an image

import matplotlib.image as mpimg

img = mpimg.imread('https://raw.githubusercontent.com/matplotlib/matplotlib.github.com/master/_images/stinkbug.png')

print(type(img))
print("Image array shape: {}".format(img.shape))

plt.imshow(img);

def low_pass(A):
    B = np.zeros_like(A)
    for i in range (373):
        for j in range(497):
            B[i,j,0] = (A[i+1,j,0] + A[i-1,j,0] + A[i,j+1,0] + A[i,j-1,0])/4
            B[i,j,1] = (A[i+1,j,1] + A[i-1,j,1] + A[i,j+1,1] + A[i,j-1,1])/4
            B[i,j,2] = (A[i+1,j,2] + A[i-1,j,2] + A[i,j+1,2] + A[i,j-1,2])/4
    return B

img1 = low_pass(img)
img2 = low_pass(img1)
img3 = low_pass(img2)
plt.imshow(img3);







