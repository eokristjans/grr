# -*- coding: utf-8 -*-

from BenchmarksV2 import * 
from TablesV2 import *

import numpy as np
import matplotlib.pyplot as plt

def grafInnsetningartimi(TIS, TIR, k, ns):
    figInnsetning, axisInnsetning = plt.subplots()
    litir1 = ['green', 'darkred', 'blue']
    litir2 = ['lightgreen', 'red', 'lightblue']
    merki = ['o', 'x', '^']
    titlarB = [' slembiröð', ' ~hækkandi röð'] 
    
    for i in range(1,k+1):
        axisInnsetning.plot(ns,TIS[i][1:4],
        marker=merki[i-1], linestyle='dashed', color=litir1[i-1], 
        linewidth=(k-i)/2+2, label=TIR[i][0]+titlarB[0])
    
    for i in range(1,k+1):
        axisInnsetning.plot(ns,TIR[i][1:4],
        marker=merki[i-1], linestyle='dashed', color=litir2[i-1],
        linewidth=(k-i)/2+1, label=TIR[i][0]+titlarB[1])
    axisInnsetning.set(xlabel='Fjöldi Innsetninga', 
                    ylabel='Tími (s)',
                    title = 'Fjöldi innsetninga á móti tíma')
    
    xs = np.arange(500, 5000, 10)
    lg = lambda x: np.log1p(x)/1000
    ys = lg(xs)
    axisInnsetning.plot(xs, ys, color='yellow', linewidth=1)
    axisInnsetning.set_ylim([0,0.055])
    plt.yticks(np.arange(0, 0.055, 0.005))
    plt.xticks(np.arange(0, 5500, 500))
    axisInnsetning.legend()
    axisInnsetning.grid()
    plt.show()
    figInnsetning.savefig('GrafInnsetningartimi.png')

grafInnsetningartimi(TaflaInnsetningartimiSlembid,
                    TaflaInnsetningartimiRadad, k, ns)


def grafLeitartimi(TS, TR, k, ms, n, t, c):
    fig, axis = plt.subplots()
    litir1 = ['green', 'darkred', 'blue']
    litir2 = ['lightgreen', 'red', 'lightblue']
    merki = ['o', 'x', '^']
    titlarB = [' slembiröð', ' ~hækkandi röð'] 
    for i in range(1,k+1):
        axis.plot(ms,TS[i][1:4],
        marker=merki[i-1], linestyle='dashed', color=litir1[i-1], 
        linewidth=(k-i)/2+2, label=TS[i][0]+titlarB[0])
    
    for i in range(1,k+1):
        axis.plot(ms,TR[i][1:4],
        marker=merki[i-1], linestyle='dashed', color=litir2[i-1],
        linewidth=(k-i)/2+1, label=TR[i][0]+titlarB[1])
    axis.set(xlabel='Fjöldi Leita', 
                    ylabel='Tími (s)',
                    title = t%n)
    
    xs = np.arange(ms[0], ms[2]+ms[0]//2, ms[0]//2)
    lg = lambda x: np.multiply(np.log1p(x),x**0.5/3000)
    ys = lg(xs)
    axis.plot(xs, ys, color='yellow', linewidth=2, label='$\sqrt{m} * ln(m) / 3000$')
    plt.xticks(np.arange(0, ms[2], ms[0]))
    plt.yticks(np.arange(0, 5, 0.5))
    axis.legend()
    axis.grid()
    plt.show()
    fig.savefig('GrafLeitartimi%d-%d.png'%(n,c))


for i in range(k):
    grafLeitartimi(TaflaArangursrikurLeitartimiSlembid[i],
               TaflaArangursrikurLeitartimiRadad[i], k, ms, ns[i],
               'Árangursrík leit í %d-staka gagnagrindum',i)
del(i)
for i in range(k):
    grafLeitartimi(TaflaArangurslitillLeitartimiSlembid[i],
               TaflaArangurslitillLeitartimiRadad[i], k, ms, ns[i],
               'Hálf-árangurslaus leit í %d-staka gagnagrindum', k+i)
del(i)

# del(merki,titlarB,litir1,litir2)

