# -*- coding: utf-8 -*-

""" Imports all variables from BenchmarksV2.py
    Alternative: import BenchmarksV2
    and refer to variables with BenchmarksV2.varname """
from BenchmarksV2 import * 

from IPython.display import HTML, display
import tabulate

# Skeytir línuheiti L fram fyrir hverja línu í T
def TaflaLinuheiti(L,T):
    for i in range(len(L)):
        T[i] = [L[i]] + T[i]
    return T

# Býr til lista af gildum með leitartíma til að birta í töflu
def LeitartimaToflur(L,T,ms):
    Ts = []
    for i in range(len(T[0])):
        Ts.append(
            TaflaLinuheiti(L, [ms
                ,T[0][i],T[1][i],T[2][i]]))
    return Ts

# Birtir staka töflu sem HTML Table í Jupyter Notebook
def BirtaTofluHTML(T,H=""):
    display(HTML("<h5>" + H + "</h5>"))
    display(HTML(tabulate.tabulate(T, tablefmt='html')))
    
# Birtir lista af töflum sem HTML Table í Jupyter Notebook
def BirtaToflurHTML(Ts,ns,H):
    for i in range(len(ns)):
        BirtaTofluHTML(Ts[i],H%ns[i])

        
""" Búa til töflur """
LinuheitiInnsetning = ['Fjöldi innsetninga','Tvíleitartré','Hrúgutré','Skopplisti']

TaflaInnsetningartimiSlembid = TaflaLinuheiti(LinuheitiInnsetning,
                            [ns,innsetningartimiTreeSlembid,
                                innsetningartimiTreapSlembid,
                                innsetningartimiSkipListSlembid])

TaflaInnsetningartimiRadad = TaflaLinuheiti(LinuheitiInnsetning,
                            [ns,innsetningartimiTreeRadad,
                                innsetningartimiTreapRadad,
                                innsetningartimiSkipListRadad])


LinuheitiLeit = ['Fjöldi leita','Tvíleitartré','Hrúgutré','Skopplisti']

tempT = [arangursrikurLeitartimiTreeSlembid, arangursrikurLeitartimiTreapSlembid, arangursrikurLeitartimiSkipListSlembid]
TaflaArangursrikurLeitartimiSlembid = LeitartimaToflur(LinuheitiLeit, tempT,ms)

tempT = [arangursrikurLeitartimiTreeRadad,arangursrikurLeitartimiTreapRadad,arangursrikurLeitartimiSkipListRadad]
TaflaArangursrikurLeitartimiRadad = LeitartimaToflur(LinuheitiLeit, tempT,ms)

tempT = [arangurslitillLeitartimiTreeSlembid, arangurslitillLeitartimiTreapSlembid, arangurslitillLeitartimiSkipListSlembid]
TaflaArangurslitillLeitartimiSlembid = LeitartimaToflur(LinuheitiLeit, tempT,ms)

tempT = [arangurslitillLeitartimiTreeRadad, arangurslitillLeitartimiTreapRadad, arangurslitillLeitartimiSkipListRadad]
TaflaArangurslitillLeitartimiRadad = LeitartimaToflur(LinuheitiLeit, tempT,ms)
del(tempT)

""" Birta töflur """
BirtaTofluHTML(TaflaInnsetningartimiSlembid, "Lyklar settir inn í slembiröð")
BirtaTofluHTML(TaflaInnsetningartimiRadad, "Lyklar settir inn í <i>~hækkandi</i> röð")

display(HTML("<h5>" + "Gagnagrindur með <i>n</i> lyklum sem voru settir inn í slembinni röð" + "</h5>"))
BirtaToflurHTML(TaflaArangursrikurLeitartimiSlembid, ns, "<i>n=</i>%d")
display(HTML("<h5>" + "Gagnagrindur með <i>n</i> lyklum sem voru settir inn í ~hækkandi röð" + "</h5>"))
BirtaToflurHTML(TaflaArangursrikurLeitartimiRadad, ns, "<i>n=</i>%d")

display(HTML("<h5>" + "Gagnagrindur með <i>n</i> lyklum sem voru settir inn í slembinni röð" + "</h5>"))
BirtaToflurHTML(TaflaArangurslitillLeitartimiSlembid, ns, "<i>n=</i>%d")
display(HTML("<h5>" + "Gagnagrindur með <i>n</i> lyklum sem voru settir inn í ~hækkandi röð" + "</h5>"))
BirtaToflurHTML(TaflaArangurslitillLeitartimiRadad, ns, "<i>n=</i>%d")