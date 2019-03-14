# -*- coding: utf-8 -*-
"""
Various Algorithms, code and notes on topics such as
    Greedy Algorithms
    Dynamic Programming 
    Randomized Programming (Monte Carlo)
Created on Sat Mar  2 11:03:42 2019

@author: Erling Oskar
"""
import numpy as np
from fractions import Fraction as frac

""" String matching """

""" Checks if a given string is a palindrome """
def isPalindrome(PP):
    P = list(PP)
    T = P.copy()
    T.reverse()
    return KMP(P,T)==0

isPalindrome("abab")

""" Compute Failure for KMP """
def ComputeFailure(P):
    F = []
    j = -1
    for i in range(len(P)):
        F.append(j)
        while j > -1 and P[i] != P[j]:
            j = F[j]
        j += 1
    return F

""" KMP (Knuth Morris Pratt) """
def KMP(TT,PP):
    T = list(TT)
    P = list(PP)
    if P==[]:
        return 0
    Fail = ComputeFailure(P)
    j = 0
    m = len(P)
    for i in range(len(T)):
        while j > -1 and T[i] != P[j]:
            j = Fail[j]
        j += 1
        if j == m:
#            print('found it')
            return i-m+1
    return -1


# Reiknar lengd samhverfra forskeyta í P.
def ComputePalindromes(P):
    if P == []:
        return [-1]
    F = []
    m = len(P)
    j = -1
    # vinnum okkur upp P
    for i in range(m):
        F.append(j)
        while j > -1 and P[i] != P[j]:
            j = F[j]
        j += 1
    # vinnum okkur aftur niður P
    for i in range(m-1,-1,-1):
        F.append(j)
        while j > -1 and P[i] != P[j]:
            j = F[j]
        j += 1
    return F


T = list("") # vinna með þetta og skoða
cpT = ComputePalindromes(T)
# Nú er lengd lengsta samhverfa forskeytisins:
min(len(T), cpT[len(cpT)-1]+1)

# túlka svo betur

S = list("abdasgea")
ComputePalindromes(S)




PP = list("abacabax") # hægt að fikta með þetta
ComputeFailure(PP)


PP
A = PP.copy()
A.reverse()
A


TT = list("faefaABRACADABRACdeafgea") # hægt að fikta með þetta
kmp = KMP(TT,PP)
kmp

list("")





""" Assignment 8 """
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
    
