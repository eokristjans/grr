# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def merge_sort(A):
    print("Splitting ",A)
    n = len(A)
    if n > 1:
        m = n // 2
        merge_sort(A[:m])
        merge_sort(A[m:])
        merge(A,m)
        
def merge(A,m):
    n = len(A)
    i, j = 0, m
    B = [0]*n
    for k in range(0,n):
        if j >= n:
            B[k] = A[i]
            i = i+1
        elif i >= m:
            B[k] = A[j]
            j = j+1
        elif A[i] < A[j]:
            B[k] = A[i]
            i = i+1
        else:
            B[k] = A[j]
            j = j+1
    for k in range(0,n):
        A[k] = B[k]
    print("Merging ",A)


mylist = [7,4,5,1,11,4,7,9]
merge_sort(mylist)