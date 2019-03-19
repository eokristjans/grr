import numpy as np
import matplotlib.pyplot as plt

def grafInnsetningartimi(LH,TIS, TIR, k, ns):
    figInnsetning, axisInnsetning = plt.subplots()
    litir1 = ['green', 'darkred', 'blue']
    litir2 = ['lightgreen', 'red', 'lightblue']
    merki = ['o', 'x', '^']
    titlarB = [' slembiröð', ' ~hækkandi röð'] 
    
    for i in range(k):
        print('Gerum feril með y-as:', ns, ', x-as:', TIS[i], 
              'merki', merki[i], 'litur', litir1[i], 'label:', LH[i+1]+titlarB[0])
        axisInnsetning.plot(ns,TIS[i],
        marker=merki[i], linestyle='dashed', color=litir1[i], 
        linewidth=(k-i)/2+2, label=LH[i+1]+titlarB[0])
    
    for i in range(k):
        print('Gerum feril með y-as:', ns, ', x-as:', TIR[i], 
              'merki', merki[i], 'litur', litir2[i], 'label:', LH[i+1]+titlarB[1])
        axisInnsetning.plot(ns,TIR[i],
        marker=merki[i], linestyle='dashed', color=litir2[i],
        linewidth=(k-i)/2+1, label=LH[i+1]+titlarB[1])
    axisInnsetning.set(xlabel='Fjöldi Innsetninga', 
                    ylabel='Tími (s)',
                    title = 'Fjöldi innsetninga á móti tíma')
    
    xs = np.arange(500, 5000, 10)
    lg = lambda x: np.log1p(x)/1000
    ys = lg(xs)
    axisInnsetning.plot(xs, ys, color='black', linewidth=1)
    
    lin = lambda x: x/100000
    ys = lin(xs)
    axisInnsetning.plot(xs, ys, color='black', linewidth=1)
    
    plt.xticks(np.arange(0, 5500, 500))
    axisInnsetning.legend()
    axisInnsetning.grid()
    plt.show()
    figInnsetning.savefig('GrafInnsetningartimi.png')


def grafLeitartimi(LH, TS, TR, k, ms, n, t, c):
    fig, axis = plt.subplots()
    litir1 = ['green', 'darkred', 'blue']
    litir2 = ['lightgreen', 'red', 'lightblue']
    merki = ['o', 'x', '^']
    titlarB = [' slembiröð', ' ~hækkandi röð'] 
    for i in range(k):
        print('Gerum feril með y-as:', ms, ', x-as:', TS[i], 
              'merki', merki[i], 'litur', litir1[i], 'label:', LH[i+1]+titlarB[0])
        axis.plot(ms,TS[i],
        marker=merki[i], linestyle='dashed', color=litir1[i], 
        linewidth=(k-i)/2+2, label=LH[i+1]+titlarB[0])
    
    for i in range(k):
        print('Gerum feril með y-as:', ms, ', x-as:', TR[i], 
              'merki', merki[i], 'litur', litir2[i], 'label:', LH[i+1]+titlarB[1])
        axis.plot(ms,TR[i],
        marker=merki[i], linestyle='dashed', color=litir2[i],
        linewidth=(k-i)/2+1, label=LH[i+1]+titlarB[1])
    axis.set(xlabel='Fjöldi Leita', 
                    ylabel='Tími (s)',
                    title = t%n)
    
    xs = np.arange(ms[0], ms[2]+ms[0]//2, ms[0]//2)
    lg = lambda x: np.log1p(x)/20
    ys = lg(xs)
    axis.plot(xs, ys, color='black', linewidth=1)
    
    lin = lambda x: x/100000
    ys = lin(xs)
    axis.plot(xs, ys, color='black', linewidth=1)
    
    plt.xticks(np.arange(0, ms[2], ms[0]))
    axis.legend()
    axis.grid()
    plt.show()
    fig.savefig('GrafLeitartimi%d-%d.png'%(n,c))

