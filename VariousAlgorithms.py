# -*- coding: utf-8 -*-
"""
Various Algorithms, code and notes on topics such as
    Greedy Algorithms
    Dynamic Programming 
    Randomized Programming (Monte Carlo)
Created on Sat Mar  2 11:03:42 2019

@author: Erling Oskar
"""










""" Assignment 8 """
import numpy as np
from fractions import Fraction as frac


def find2(A):
    found = False
    k = 0
    while (not found):
        i = np.random.randint(1,4)
        k+=1
        if i == 2:
            found = True
    A.append(k)

A = []
for i in range(1000000):
    find2(A)

B = []
for i in range(max(A)):
    b = 0
    for j in range(len(A)):
        if A[j] == i:
            b += 1
    B.append(b/len(A))
    
print(B)

for j in range(len(B)):
    print(B[j])
    

c = frac(2,3)
c0 = frac(0,1)
for i in range(100):
    c0 += c**i
    print(c0)
    
