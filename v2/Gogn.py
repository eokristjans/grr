# -*- coding: utf-8 -*-
"""

@author: Erling Oskar
"""
import numpy as np
import random
import time

from Treap import Treap
from Tree import Tree

"""
Búum til gögn fyrir innsetningu
"""
def RandomVixlanir(X,n):
    for i in range(n//10):
        a, b = random.randint(0,n-1), random.randint(0,n-1)
        X[a], X[b] = X[b], X[a]

ns = [500, 2000, 5000, 10000]

SlembnirLyklar = []
i = 0
for n in ns:
    SlembnirLyklar.append(np.arange(1, 2*n+1, 2))
    random.shuffle(SlembnirLyklar[i])
    i+=1
del(i)

RadadirLyklar = []
i = 0
for n in ns:
    RadadirLyklar.append(np.arange(1, 2*n+1, 2))
    RandomVixlanir(RadadirLyklar[i], n)
    i+=1
del(i)

"""
Byrjum að tímamæla innsetningar

https://docs.python.org/3/library/time.html#time.perf_counter
    Vert að skoða:
time.process_time() # telur ekki svefntíma
time.process_time_ns() # telur ekki svefntíma
time.perf_counter() # telur svefntíma með
time.perf_counter_ns() # telur svefntíma með
time.thread_time()
time.thread_time_ns()
"""
def MaelaInnsetningartima(ds, Xs):
    timi = []
    for X in Xs:
        start = time.clock()
        for x in X:
            ds.insert(x)
        end = time.clock()
        timi.append((end-start))
    return timi
""" HELD ÞAÐ SÉ EKKI VERIÐ AÐ ÝTRA Í GEGNUM GAGNAGRINDURNAR """

TreapS, TreapR = [Treap()] * len(ns), [Treap()] * len(ns)
innsetningartimiTreapS = MaelaInnsetningartima(TreapS,SlembnirLyklar)
innsetningartimiTreapR = MaelaInnsetningartima(TreapR,RadadirLyklar)

TreeS, TreeR = [Tree(1)] * len(ns), [Tree(1)] * len(ns)
innsetningartimiTreeS = MaelaInnsetningartima(TreeS,SlembnirLyklar)
innsetningartimiTreeR = MaelaInnsetningartima(TreeR,RadadirLyklar)

""" BÆTA VIÐ FYRIR SKIP LIST """



"""
Búum til gögn fyrir leit
"""
def MaelaLeitartima(ds, Xs):
    timi = []
    for X in Xs:
        start = time.clock()
        for x in X:
            ds.contains(x)
        end = time.clock()
        timi.append((end-start))
    return timi

ms = [50000, 100000, 200000, 400000]


leitartimiTreapS = MaelaLeitartima(TreapS, SlembnirLyklar, ms)
leitartimiTreapR = MaelaLeitartima(TreapR, RadadirLyklar, ms)

# Með hálfum árangri.
# Afrita fylki með gögnum og bæta við stökum.
# Leita svo.
leitartimiTreapS = MaelaLeitartima(TreapS, SlembnirLyklar, ms)
leitartimiTreapR = MaelaLeitartima(TreapR, RadadirLyklar, ms)










