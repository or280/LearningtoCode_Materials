#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:30:17 2021

@author: Ollie

Title: Dice
"""

import numpy


def diceroll(s,n,m):
    rolls = []
    counter = 0
    for i in range(n):
        value = numpy.random.randint(1,s+1)
        rolls.append(value)
        if value >= m:
            counter += 1
        
    return rolls, counter
    
    
    
print (diceroll(6,12,4))

