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

print(ComputeFailure(list("abbaabba")))



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
    Ts.append(t)
    for s in range(n-m+1):
        if p == t:
            if P == T[s:s+m]:
                return s, falseMatch, Ts
            falseMatch += 1
        t = (10 * (t - (sigma*T[s] % q) % q) % q) + T[s+m] % q
        Ts.append(t)
    return -1, falseMatch, Ts
    
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


# Ákvarðar lengsta samhverfra forskeyti P
# Byggt á KMP og ComputeFailure
def ComputePalindrome(P):
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
    lengdSamhverfu = min(len(P),F[len(F)-1]+1)
    return P[:lengdSamhverfu]


def main():
    T = list("ABRARBACADABRX") # vinna með þetta og skoða
    cpT = ComputePalindrome(T)
    # Nú er lengd lengsta samhverfa forskeytisins:
    print('lengsta samhverfa forskeyti listans/strengsins \n' + str(T) + '\n er ' + str(cpT))

main()





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
    
