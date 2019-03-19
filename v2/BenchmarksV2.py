""""""""""""""" global imports """""""""""""""
import numpy as np

""""""""""""""" local imports """""""""""""""
from Treap import Treap
from Tree import Tree
from SkipList import SkipList
from FunctionsV2 import SmidaInnsetningarLyklaLista, SmidaLeitarLyklaLista
from FunctionsV2 import MaelaInnsetningartima, MaelaLeitartima
from TablesV2 import TaflaLinuheiti, LeitartimaToflur, BirtaTofluHTML, BirtaToflurHTML
from GraphsV2 import grafInnsetningartimi, grafLeitartimi


""""""""""""""" Fjöldi mælinga """""""""""""""
k = 3
ns = [500, 2500, 5000]
ms = [100000, 200000, 400000]
f = 50 # fjöldi mælinga


""""""""""""""" Listar undir innsetningartíma """""""""""""""
innsetningartimiTreeSlembid = np.zeros(3,dtype=float)
innsetningartimiTreeRadad = np.zeros(3,dtype=float)
innsetningartimiTreapSlembid = np.zeros(3,dtype=float)
innsetningartimiTreapRadad = np.zeros(3,dtype=float)
innsetningartimiSkipListSlembid = np.zeros(3,dtype=float)
innsetningartimiSkipListRadad = np.zeros(3,dtype=float)
# Og setja þá í lista til að geta vísað í þá eftir stuðlum

""""""""""""""" Listar undir leitartíma """""""""""""""
arangursrikurLeitartimiTreeSlembid = np.zeros((3,3),dtype=float)
arangursrikurLeitartimiTreeRadad = np.zeros((3,3),dtype=float)
arangursrikurLeitartimiTreapSlembid = np.zeros((3,3),dtype=float)
arangursrikurLeitartimiTreapRadad = np.zeros((3,3),dtype=float)
arangursrikurLeitartimiSkipListSlembid = np.zeros((3,3),dtype=float)
arangursrikurLeitartimiSkipListRadad = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiTreeSlembid = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiTreeRadad = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiTreapSlembid = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiTreapRadad = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiSkipListSlembid = np.zeros((3,3),dtype=float)
arangurslitillLeitartimiSkipListRadad = np.zeros((3,3),dtype=float)

""" Smíða gögn til að leita að """
ArangursrikirLyklar = SmidaLeitarLyklaLista(ms[2], ns, k, False)
ArangurslitlirLyklar = SmidaLeitarLyklaLista(ms[2], ns, k, True)

""" Mælingar geta hafist """
for i in range(f):
    """ Smíða gögn til innsetningar """
    SlembnirLyklar = []
    RadadirLyklar = []
    SmidaInnsetningarLyklaLista(SlembnirLyklar, RadadirLyklar, ns)
    
    """"""""""""""" Mælingar á innsetningartíma """""""""""""""
    """ Setja gögn í gagnagrindur """
    TreeS = [Tree(SlembnirLyklar[0][0]), Tree(SlembnirLyklar[1][0]), Tree(SlembnirLyklar[2][0])]
    TreeR = [Tree(RadadirLyklar[0][0]), Tree(RadadirLyklar[1][0]), Tree(RadadirLyklar[2][0])]
    MaelaInnsetningartima(TreeS,SlembnirLyklar,k,innsetningartimiTreeSlembid)
    MaelaInnsetningartima(TreeR,RadadirLyklar,k,innsetningartimiTreeRadad)
    
    TreapS = [Treap(),Treap(),Treap()]
    TreapR = [Treap(),Treap(),Treap()]
    MaelaInnsetningartima(TreapS,SlembnirLyklar,k,innsetningartimiTreapSlembid)
    MaelaInnsetningartima(TreapR,RadadirLyklar,k,innsetningartimiTreapRadad)
    
    SkipListS = [SkipList(), SkipList(), SkipList()]
    SkipListR = [SkipList(), SkipList(), SkipList()]
    MaelaInnsetningartima(SkipListS,SlembnirLyklar,k,innsetningartimiSkipListSlembid)
    MaelaInnsetningartima(SkipListR,RadadirLyklar,k,innsetningartimiSkipListRadad)
    
    """"""""""""""" Mælingar á leitartíma """""""""""""""
    """ Leitad ad lyklum sem eru i gagnagrindunum """
    MaelaLeitartima(TreeS, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiTreeSlembid)
    MaelaLeitartima(TreeR, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiTreeRadad)
    
    MaelaLeitartima(TreapS, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiTreapSlembid)
    MaelaLeitartima(TreapR, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiTreapRadad)
    
    MaelaLeitartima(SkipListS, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiSkipListSlembid)
    MaelaLeitartima(SkipListR, ArangursrikirLyklar, ms, k, arangursrikurLeitartimiSkipListRadad)

    """ Leitad ad lyklum þar sem helmingur er i gagnagrindunum """
    MaelaLeitartima(TreeS, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiTreeSlembid)
    MaelaLeitartima(TreeR, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiTreeRadad)
    
    MaelaLeitartima(TreapS, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiTreapSlembid)
    MaelaLeitartima(TreapR, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiTreapRadad)
    
    MaelaLeitartima(SkipListS, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiSkipListSlembid)
    MaelaLeitartima(SkipListR, ArangurslitlirLyklar, ms, k, arangurslitillLeitartimiSkipListRadad)
    
""" Deila tímamælingum með fjölda tímamælinga """
innsetningartimiTreeSlembid *= (1/f)
innsetningartimiTreeRadad *= (1/f)
innsetningartimiTreapSlembid *= (1/f)
innsetningartimiTreapRadad *= (1/f)
innsetningartimiSkipListSlembid *= (1/f)
innsetningartimiSkipListRadad *= (1/f)

arangursrikurLeitartimiTreeSlembid *= (1/f)
arangursrikurLeitartimiTreeRadad *= (1/f)
arangursrikurLeitartimiTreapSlembid *= (1/f)
arangursrikurLeitartimiTreapRadad *= (1/f)
arangursrikurLeitartimiSkipListSlembid *= (1/f)
arangursrikurLeitartimiSkipListRadad *= (1/f)
arangurslitillLeitartimiTreeSlembid *= (1/f)
arangurslitillLeitartimiTreeRadad *= (1/f)
arangurslitillLeitartimiTreapSlembid *= (1/f)
arangurslitillLeitartimiTreapRadad *= (1/f)
arangurslitillLeitartimiSkipListSlembid *= (1/f)
arangurslitillLeitartimiSkipListRadad *= (1/f)

# Setja tímamælingar í lista
IT = [innsetningartimiTreeSlembid
, innsetningartimiTreeRadad
, innsetningartimiTreapSlembid
, innsetningartimiTreapRadad
, innsetningartimiSkipListSlembid
, innsetningartimiSkipListRadad]

LT = [arangursrikurLeitartimiTreeSlembid
, arangursrikurLeitartimiTreeRadad
, arangursrikurLeitartimiTreapSlembid
, arangursrikurLeitartimiTreapRadad
, arangursrikurLeitartimiSkipListSlembid
, arangursrikurLeitartimiSkipListRadad
, arangurslitillLeitartimiTreeSlembid
, arangurslitillLeitartimiTreeRadad
, arangurslitillLeitartimiTreapSlembid
, arangurslitillLeitartimiTreapRadad
, arangurslitillLeitartimiSkipListSlembid
, arangurslitillLeitartimiSkipListRadad]

# Notað fyrir heiti í töflum og gröfum
LinuheitiInnsetning = ['Fjöldi innsetninga','Tvíleitartré','Hrúgutré','Skopplisti']
LinuheitiLeit = ['Fjöldi leita','Tvíleitartré','Hrúgutré','Skopplisti']


""""""""" Búa til töflur """""""""
TaflaInnsetningartimiSlembid = TaflaLinuheiti(LinuheitiInnsetning,[ns,IT[0],IT[2],IT[4]])
TaflaInnsetningartimiRadad = TaflaLinuheiti(LinuheitiInnsetning,[ns,IT[1],IT[3],IT[5]])
TaflaArangursrikurLeitartimiSlembid = LeitartimaToflur(LinuheitiLeit, [LT[0], LT[2], LT[4]],ms)
TaflaArangursrikurLeitartimiRadad = LeitartimaToflur(LinuheitiLeit, [LT[1], LT[3], LT[5]],ms)
TaflaArangurslitillLeitartimiSlembid = LeitartimaToflur(LinuheitiLeit, [LT[6], LT[8], LT[10]],ms)
TaflaArangurslitillLeitartimiRadad = LeitartimaToflur(LinuheitiLeit, [LT[7], LT[9], LT[11]],ms)

""" Birta töflur - Líklega hægt að búa til töflur án þess að birta þær. Allavega tabulate """
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



def buaTilToflu(table,headers):
    (tabulate(table, headers, tablefmt="html"))




"""
Notuðum `timeit()` sem notar `time.perf_counter()` (`perf` fyrir _perfomance_), sem
skilar fleytitölu og er nákvæmasti kosturinn í stuttar mælingar samkvæmt Python Docs.
Mælingin inniheldur tímann sem líður þegar þráðurinn sefur, en það sýnir góða 
mynd af notkun í raunveruleikanum. Þetta er svipað og að taka mismun á tveimur
mælingum af tímanum sem hefur liðið síðan epoch, en þessi aðferð á að vera 
nákvæmari á Windows stýrikerfum.
"""






""""""""" Búa til línurit """""""""
grafInnsetningartimi(LinuheitiInnsetning,[IT[0], IT[2], IT[4]],
                    [IT[1], IT[3], IT[5]], k, ns)
for i in range(k):
    grafLeitartimi(LinuheitiLeit, LT[i], LT[i+1], k, ms, ns[i],
               'Árangursrík leit í %d-staka gagnagrindum',i)
for i in range(k):
    grafLeitartimi(LinuheitiLeit, LT[2*k+i], LT[2*k+i+1], k, ms, ns[i],
               'Hálf-árangurslaus leit í %d-staka gagnagrindum', k+i)



""" Before data is exported
del(TreeS,TreeR,SkipListS,SkipListR,TreapS,TreapR)
del(ArangurslitlirLyklar,ArangursrikirLyklar,RadadirLyklar,SlembnirLyklar)
"""







