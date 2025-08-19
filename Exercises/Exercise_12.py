#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:59:23 2020

Title: Exercise 9

@author: Oliver Reed
"""
# Class of a vector

import numpy as np

class MyVector:
    """A vector object that can return its size and norm, and can compute the dot product 
    with another vector  """
    
    def __init__(self, x):
        self.x = x
        
    def size(self):
        return len(self.x)
        
    def __getitem__(self, index):
        return self.x[index]
    
    def norm(self):
       ans = 0
       for i in self.x:
           ans += i**2
       return np.sqrt(ans)
    
    def dot(self, other):
        ans = 0
        for i in range(len(self.x)):
            ans += self.x[i] * other.x[i]
        return ans
    

u = MyVector([1, 1, 2])
v = MyVector([2, 1, 1])


print(u.size())
print(u.norm())
print(u.dot(v))




import datetime 

class StudentEntry:
    def __init__(self, surname, forename, birth_year, year, college, crsid=None):
        self.surname = surname
        self.forename = forename
        self.birth_year = birth_year
        self.year = year
        self.college = college
        self.crsid = crsid
        
        
    def age(self):
        year = datetime.date.today().year
        ans = year - self.birth_year
        return ans
    
    def __repr__(self):
        print ("Surname: " + self.surname + ", Forename: " + self.forename + ", College: " + self.college)

    def __lt__(self, other):
        if self.surname == other.surname:
            list = [self.forename, other.forename] 
            list.sort()
            if list[0] == self.forename:
                return True
            else:
                return False
        else:
            list = [self.surname, other.surname] 
            list.sort()
            if list[0] == self.surname:
                return True
            else:
                return False
                             
            


s0 = StudentEntry("Bloggs", "Andrea", 1996, 1, "Churchill", "ab1001")       
s1 = StudentEntry("Reali", "John", 1997, 1, "Corpus Christi")       
s2 = StudentEntry("Bacon", "Kevin", 1996, 1, "Newnham")
s3 = StudentEntry("Bacon", "Alexander", 1996, 1, "Queens")


print (StudentEntry.__repr__(s1))


print(s0 < s1)
print(s0 > s2)
print(s3 < s2)




