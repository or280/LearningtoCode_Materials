#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:10:42 2021

@author: Ollie

Title: XRD Fitting, positions
"""

import numpy as np
import csv
from scipy.optimize import minimize
import matplotlib.pyplot as plt


with open('Ti20Nb4Sn_900_30min_AC.csv', newline='') as csvfile:
     csvdata = csv.reader(csvfile, delimiter=' ')
     data = {}
     for row in csvdata:
         data[row[0]] = float(row[1])


xdata = []
ydata = []

for i in data.keys():
    xdata.append(float(i))

for i in data.values():
    ydata.append(i)
    
print (xdata)
print (ydata)

# Define standard width and intensity for each peak, so we will only fit the positions.
w = 0.1
I = 15

def sumres(x):
    sumres = 0
    ymodel = []
    for i in range(len(ydata)):
        f = I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[0])**2)/(2*w**2)) + I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[1])**2)/(2*w**2)) + I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[2])**2)/(2*w**2)) + I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[3])**2)/(2*w**2)) + I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[4])**2)/(2*w**2))
        ymodel.append(f)
        sumres += (ymodel[i]-ydata[i])**2
    return sumres
    
    
print(sumres([39,55,70,83,95]))

res = minimize(sumres,[39,55,70,83,95])

v=res.x

ymodel = []
for i in range(0,len(xdata)):
    ymodel.append(I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[0])**2)/(2*w**2)) +
                  I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[1])**2)/(2*w**2)) +
                  I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[2])**2)/(2*w**2)) +
                  I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[3])**2)/(2*w**2)) +
                  I/(w * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[4])**2)/(2*w**2)))
    
plt.plot(xdata,ydata)
plt.plot(xdata,ymodel)

print(res)



