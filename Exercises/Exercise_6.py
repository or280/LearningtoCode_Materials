#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:33:00 2020

Title: Exercise 6

@author: Oliver Reed
"""


# Function to find area of a triangle using lists.

x0=0.0
y0=0.0
x1=0.0
y1=2.0
x2=3.0
y2=0.0

vertices = [x0,y0,x1,y1,x2,y2]

def triangle_area(v):
    area = (v[0]*(v[3] - v[5]) + v[2]*(v[5] - v[1]) + v[4]*(v[1] - v[3]))*0.5
    print(abs(area))
    
triangle_area(vertices)
        
# Function to add
x = [0,0,3,4,5]
y = [0,2,0,6,3]

def area(a,b):
    if len(a) != len(b):
        raise RuntimeError('lists a and b of different lengths')
    area = 0
    for i in range(len(a)-1):
        area += 0.5*(abs(a[i]*b[i+1]-a[i+1]*b[i])) 
        
    return area

print(area(x,y))

# Function to add 2 vectors of arbitary length.

def vector_add(x,y):
    if len(x) != len(y):
        print ("lengths do not match, please enter other vectors")
    else:
        z = []
        for i in range(len(x)):
            z.append(x[i]+y[i])
        return z
    
a = [3,4,5]
b = [0,3,4]

c = vector_add(a,b)
print(c)



# Colleges dictionary.
import numpy as np

colleges = {"Pembroke": ["Pem", 500, 1347], "Peterhouse": ["Pet", 300, 1331], "Trinity": ["Tri", 1000, 1393]}

def no_stud(dic, key):
    l = dic[key]
    return l[1]



def top(college):
    no_students = []
    for key in college: 
        no_students.append(no_stud(college,key))
                            
    np.sort(no_students)
    
    for keys in college:
        if (no_students[len(no_students)-1]) == no_stud(college,keys):
            return (college[keys])[0]
    
    

print(top(colleges))






