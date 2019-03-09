# -*- coding: utf-8 -*-
"""
Various Algorithms, code and notes on topics such as
    Greedy Algorithms
    Dynamic Programming 
    Randomized Programming (Monte Carlo)
Created on Sat Mar  2 11:03:42 2019

@author: Erling Oskar
"""



""" Assignment 9 """
# Checks whether P is a sublist of T
# T and P are lists of numbers, len(T)=n, len(P)=m
# Returns (s, falseMatch, ts)
#  where s = -1 if P is not a sublist of T,
#    else s is the number for which P == T[s:s+m]
#  falseMatch is the number of false matches found during the search
#  ts are all the t_s calculated during the search
def KarpRabin(T,P):
    n = len(T)
    m = len(P)
    q = 11
    sigma = 10**(len(P)-1) % q
    p = t = 0
    falseMatch = 0
    Ts = []
    for i in range(m):
        p = (10*p % q) + P[i] % q
        t = (10*t % q) + T[i] % q
    ts.append(t)
    for s in range(n-m+1):
        if p == t:
            if P == T[s:s+m]:
                return s, falseMatch, ts
            falseMatch += 1
        t = (10 * (t - (sigma*T[s] % q) % q) % q) + T[s+m] % q
        Ts.append(t)
    return -1, falseMatch, ts
    
TTs = "1414213562373095"
TT = [int(i) for i in TTs]
PPs = "730"
PP = [int(i) for i in PPs]
KR = KarpRabin(TT,PP)
print('Er', PPs, 'hlutstrengur i', TTs, '?', (KR[0]!=-1))
print('Rangar paranir:', KR[1])
Ts = ""
for i in KR[2]:
    Ts += str(i) + " "
print('ts gildin eru: ', Ts)






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
    
