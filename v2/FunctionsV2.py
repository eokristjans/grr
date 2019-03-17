# -*- coding: utf-8 -*-
"""

@author: Erling Oskar
"""
import numpy as np
import random
import time

""""""""" Búa til gögn fyrir innsetningu """""""""
def SmidaInnsetningarLyklaLista(Ss, Rs, ns):
    i = 0
    for n in ns:
        Ss.append(np.arange(1, 2*n+1, 2))
        Rs.append(np.copy(Ss[i]))
        random.shuffle(Ss[i])
        RandomVixlanir(Rs[i], n)
        i+=1

""""""""" Búa til gögn fyrir leit """""""""
def SmidaLeitarLyklaLista(m, ns, k, b):
    Ls = []
    for i in range(k):
        n = ns[i]
        a = np.arange(0, 2*n) if b else np.arange(1, 2*n+1, 2)
        Ls.append(a)
        while len(Ls[i]) < m:
            Ls[i] = np.concatenate((Ls[i], a))
        random.shuffle(Ls[i])
    return Ls
    
    
"""    
    else:
        
    #    print(len(Ls[i]), ':', min(Ls[i]), '-', max(Ls[i]))
        # Add additional unsuccessful search keys
        while len(Ls[i]) < m:
            A = np.arange(3*ns[i]+1, 4*ns[i]+1, 1)
            B = np.arange(-2*ns[i], -1*ns[i], 1)
            Ls[i] = np.concatenate((Ls[i], A))
            Ls[i] = np.concatenate((Ls[i], B))
    #    print(len(Ls[i]), ':', min(Ls[i]), '-', max(Ls[i]))
        random.shuffle(Ls[i])
    return Ls
"""

def RandomVixlanir(X,n):
    for i in range(n//10):
        a, b = random.randint(0,n-1), random.randint(0,n-1)
        X[a], X[b] = X[b], X[a]



"""
https://docs.python.org/3/library/time.html#time.perf_counter
    Vert að skoða:
time.process_time() # telur ekki svefntíma
time.process_time_ns() # telur ekki svefntíma
time.perf_counter() # telur svefntíma með
time.perf_counter_ns() # telur svefntíma með
time.thread_time()
time.thread_time_ns()
"""
""" Tímamæla innsetningar 
    Tekur meðaltal af f mælingum
"""
def MaelaInnsetningartima(DSs, Xs, k, f=10):
    Timi = []
    for i in range(k):
        timi = 0
        for j in range(f):
            start = time.clock()
            for x in Xs[i]:
                DSs[i].insert(x)
            end = time.clock()
            timi += (end-start)
        Timi.append((timi/f))
    return Timi

""" Tímamæla leit 
    Tekur meðaltal af f mælingum
Fyrir:  k er fjöldi gagnagrinda (sem á að leita í)
        DSs er k-staka listi af gagnagrindum
        Xs er k-staka listi af listum af lyklum
        ms er 3ja staka talnalisti (fjöldi leitanna)
Eftir:  timi er listi af listum
        timi[i] inniheldur tímann fyrir ms[0], ms[1] og ms[2] leitanir í DSs[i]
"""
def MaelaLeitartima(DSs, Xs, ms, k, f=10):
    Timi = []
    for i in range(k):
        Timi.append([])
        t = [0, 0, 0]
        for u in range(f):
            start = time.clock()
            for j in range(ms[0]):
                DSs[i].contains(Xs[i][j])
            end = time.clock()
            t[0] += (end-start)
            for j in range(ms[0],ms[1]):
                DSs[i].contains(Xs[i][j])
            end = time.clock()
            t[1] += (end-start)
            for j in range(ms[1],ms[2]):
                DSs[i].contains(Xs[i][j])
            end = time.clock()
            t[2] += (end-start)
        for T in t:
            print(T, ' ', u)
        Timi[i].append(t[0]/f)
        Timi[i].append(t[1]/f)
        Timi[i].append(t[2]/f)
    return Timi

