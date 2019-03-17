""""""""""""""" global imports """""""""""""""
import numpy as np
import random

""""""""""""""" local imports """""""""""""""
from Treap import Treap
from Tree import Tree
from SkipList import SkipList
from FunctionsV2 import SmidaInnsetningarLyklaLista, SmidaLeitarLyklaLista
from FunctionsV2 import MaelaInnsetningartima, MaelaLeitartima


""""""""""""""" Fjöldi mælinga """""""""""""""
k = 3
ns = [500, 2500, 5000]
ms = [100000, 200000, 400000]



""""""""""""""" Mælingar á innsetningartíma """""""""""""""
""" Smíða gögn til innsetningar """
SlembnirLyklar = []
RadadirLyklar = []
SmidaInnsetningarLyklaLista(SlembnirLyklar, RadadirLyklar, ns)

""" Setja gögn í gagnagrindur """
TreeS = [Tree(SlembnirLyklar[0][0]), Tree(SlembnirLyklar[1][0]), Tree(SlembnirLyklar[2][0])]
TreeR = [Tree(RadadirLyklar[0][0]), Tree(RadadirLyklar[1][0]), Tree(RadadirLyklar[2][0])]
innsetningartimiTreeSlembid = MaelaInnsetningartima(TreeS,SlembnirLyklar,k)
innsetningartimiTreeRadad = MaelaInnsetningartima(TreeR,RadadirLyklar,k)

TreapS = [Treap(),Treap(),Treap()]
TreapR = [Treap(),Treap(),Treap()]
innsetningartimiTreapSlembid = MaelaInnsetningartima(TreapS,SlembnirLyklar,k)
innsetningartimiTreapRadad = MaelaInnsetningartima(TreapR,RadadirLyklar,k)


SkipListS = [SkipList(), SkipList(), SkipList()]
SkipListR = [SkipList(), SkipList(), SkipList()]
innsetningartimiSkipListSlembid = MaelaInnsetningartima(SkipListS,SlembnirLyklar,k)
innsetningartimiSkipListRadad = MaelaInnsetningartima(SkipListR,RadadirLyklar,k)


""""""""""""""" Mælingar á leitartíma """""""""""""""
""" Smíða gögn til að leita að """
ArangursrikirLyklar = SmidaLeitarLyklaLista(ms[2], ns, k, False)
ArangurslitlirLyklar = SmidaLeitarLyklaLista(ms[2], ns, k, True)


""" Leitad ad lyklum sem eru i gagnagrindunum """
arangursrikurLeitartimiTreeSlembid = MaelaLeitartima(
                                        TreeS, ArangursrikirLyklar, ms, k)
arangursrikurLeitartimiTreeRadad = MaelaLeitartima(
                                        TreeR, ArangursrikirLyklar, ms, k)

arangursrikurLeitartimiTreapSlembid = MaelaLeitartima(
                                        TreapS, ArangursrikirLyklar, ms, k)
arangursrikurLeitartimiTreapRadad = MaelaLeitartima(
                                        TreapR, ArangursrikirLyklar, ms, k)

arangursrikurLeitartimiSkipListSlembid = MaelaLeitartima(
                                        SkipListS, ArangursrikirLyklar, ms, k)
arangursrikurLeitartimiSkipListRadad = MaelaLeitartima(
                                        SkipListR, ArangursrikirLyklar, ms, k)


""" Leitad ad lyklum þar sem helmingur er i gagnagrindunum """
arangurslitillLeitartimiTreeSlembid = MaelaLeitartima(
                                        TreeS, ArangurslitlirLyklar, ms, k)
arangurslitillLeitartimiTreeRadad = MaelaLeitartima(
                                        TreeR, ArangurslitlirLyklar, ms, k)

arangurslitillLeitartimiTreapSlembid = MaelaLeitartima(
                                        TreapS, ArangurslitlirLyklar, ms, k)
arangurslitillLeitartimiTreapRadad = MaelaLeitartima(
                                        TreapR, ArangurslitlirLyklar, ms, k)

arangurslitillLeitartimiSkipListSlembid = MaelaLeitartima(
                                        SkipListS, ArangurslitlirLyklar, ms, k)
arangurslitillLeitartimiSkipListRadad = MaelaLeitartima(
                                        SkipListR, ArangurslitlirLyklar, ms, k)