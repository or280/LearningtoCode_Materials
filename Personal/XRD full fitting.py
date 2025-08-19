#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:10:42 2020

@author: Ollie

Title: XRD full fitting
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


def sumres(x):
    sumres = 0
    ymodel = []
    for i in range(len(ydata)):
        f = x[0]+x[1]*xdata[i] + x[2]/(x[3] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[4])**2)/(2*x[3]**2)) + x[5]/(x[6] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[7])**2)/(2*x[6]**2)) + x[8]/(x[9] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-x[10])**2)/(2*x[9]**2))
        ymodel.append(f)
        sumres += (ymodel[i]-ydata[i])**2
    return sumres
    
    
print(sumres([0.26,0.07,50,0.16,39,20,0.2,55,36,0.18,70]))

res = minimize(sumres,[0.26,0.07,50,0.16,39,20,0.2,55,36,0.18,70])

v=res.x

ymodel = []
for i in range(0,len(xdata)):
    ymodel.append(v[0]+v[1]*xdata[i] +
                  v[2]/(v[3] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[4])**2)/(2*v[3]**2)) +
                  v[5]/(v[6] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[7])**2)/(2*v[6]**2)) +
                  v[8]/(v[9] * (2*3.14159)**0.5)*np.exp(-((xdata[i]-v[10])**2)/(2*v[9]**2)))
    
plt.plot(xdata,ydata)
plt.plot(xdata,ymodel)

print(res)





