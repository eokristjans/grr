# -*- coding: utf-8 -*-
"""
Namskeid:   Greining Reiknirita tol403
Kennari:    Hjalmtyr Hafsteinsson
Stofnun:    Haskoli Islands
Höfundur:   Erling Oskar Kristjansson

------------------------------------------------------------------------------

NOTKUNARLYSING:
v1.py er lausn a Verkefni 1 i ofangreindu namskeidi.
Keyra skal forritid sem eina heild, thvi thad notast vid vidvaerar breytur sem
annars gaetu ruglast nema notandi þekki adferdirnar og breyturnar ur forritinu.
Forritid prentar videigandi nidurstodur.

  I forritinu er buid ad kommenta ut kall a adferdina kostnadurEndurkvaemt(),
thar sem keyrslutimi thess er of langur, og thad er onaudsynleg vidbot.
  Einnig er buid ad kommenta ut kall a adferdina KostnadurStoppaOllumHotelum(),
sem reiknar kostnadinn vid ad stoppa og gista a ollum hotelum, en er haegt ad
baeta vid til samanburdar vid Graduga Reikniritid og Kviku Bestunarlausnina.
  Einnig framleidir og skilar adferdin fDreifdHotel(..) auka tuple sem er
ekki notad vid utreikninga, en getur verid gagnlegt og frodlegt ad glugga i.

"""
import random
import numpy as np
  
'''''''''''''''''''''''''Adferdir vid mat a kostnadi'''''''''''''''''''''''''

''''''''''''''' Hjalparfoll '''''''''''''''
''' Skilar fjarlaegd milli hotela numer i og j '''
fjarlaegd = lambda i,j : np.abs((hotelfylki[j] - hotelfylki[i]))
''' Skilar kostnadinum vid ad ferdast fjarlaegd x '''
kostnadur = lambda x : (200 - x)**2


''' Notar endurkvaemni til ad reikna minnsta kostnad 
vid ad ferdast fra hoteli numer ii til hotels jj
Hryllilega haegvirkt, ekki radlagt ad keyra
ef vidvaera breytan hotelfjoldi er > 25 '''
def KostnadurEndurkvaemt(ii,jj):
    kjj = kostnadur(fjarlaegd(ii,jj))
    if jj == hotelfjoldi:
        return kjj
    else:
        return min( KostnadurEndurkvaemt(ii,jj+1),
            kjj + KostnadurEndurkvaemt(jj,jj+1))

''' Reiknar kostnadinn midad vid ad solumadurinn gisti a ollum hotelum '''
def KostnadurStoppaOllumHotelum():
    sumsofar = 0
    kostn = [0]
    for i in range(1,stadafjoldi):
        sumsofar += kostnadur(fjarlaegd(i-1,i))
        kostn.append(sumsofar)
    return tuple(kostn)

''' "Gráðuga reikniritið á bara að reyna að besta næsta stopp,
         og ekki að horfa neitt fram í tímann."
Gradugt reiknirit(adferd) sem gerir akkurat thad:
  Itrar yfir moguleg hotel og velur besta skrefid i hverju skrefi. '''
def kostnadurGradugt():
    gradKostn = 0
    gradSkref = 0
    i = gradSkref
    while i < hotelfjoldi:
        gradSkref += 1
        ki = kostnadur(fjarlaegd(i,gradSkref))
        for j in range(i+2, stadafjoldi):
            kij = kostnadur(fjarlaegd(i,j))
            if kij <= ki:
                gradSkref = j
                ki = kij
        gradKostn += ki
        i = gradSkref
#        print(i)       # Prentar hotelin sem verda fyrir valinu
    return gradKostn

'''
Adferd sem notar kvika bestun til ad reikna laegsta heildarkostnad ferdarinnar.
Notkun:  kb = KostnadurKB()
Eftir:   kb er tuple sem inniheldur laegsta kostnadinn til midad vid ad
         serhvert hotel a bilini [1,hotelfjoldi] geti verid sidasta hotelid.
             kb[hotelfjoldi] inniheldur tvi laegsta heildarkostnad ferdarinnar
'''
def KostnadurKB():
    minKostn = [0]
    k1 = kostnadur(fjarlaegd(0,1))
    minKostn.append(k1)
    for j in range(2,stadafjoldi):
        kj = kostnadur(fjarlaegd(j-1,j)) + minKostn[j-1]
        for i in range(j-2,-1,-1):    # fra j-2 nidri 0
            kij = kostnadur(fjarlaegd(i,j)) + minKostn[i]
            kj = min(kij,kj)
        minKostn.append(kj)
    return tuple(minKostn)
            

'''''''''''''''  V1 - Gerd gagna  '''''''''''''''
'''
Notkun  h = fDreifdHotel(aa,bb,nn,f)
Fyrir:  nn er heiltala
        f er tviundaradgerd sem skilar tolu
        aa og bb eru breytur af gerd sem f raedur vid
Eftir:  h er tuple med tveimur tuples
        h[0] eru nn tolur framkalladar med f(aa,bb)
        h[1] eru nn+1 tolur, nefnilega
    h[1] = [0, h[0][0], h[0][0]+h[0][1], ..., h[0][0]+...+h[0][nn-1]]
'''
def fDreifdHotel(aa,bb,nn,f):
    AA = [0]
    BB = []
    for i in range(nn):
        BB.append(f(aa,bb))
        AA.append(AA[i]+BB[i])
    return tuple(BB),tuple(AA)
    
unf = lambda a,b : random.uniform(a,b)
nmork, emork        = 100, 300
hotelfjoldi         = 100
stadafjoldi         = hotelfjoldi+1
hotel               = fDreifdHotel(nmork,emork,hotelfjoldi,unf)
hotelfjarlaegdir    = hotel[0]
hotelfylki          = hotel[1]
''''''''''''''''''''''''''''''''''''''''''''''''

kostnadurKB0 = KostnadurKB()
# kostnadurStoppaOllumHotelum0 = KostnadurStoppaOllumHotelum()
kostnadurGradugt0 = kostnadurGradugt()

print('Nidurstada med', hotelfjoldi, 'hotel thar sem fjarlaegd a milli hotela er jafndeifd slembitala a milli', nmork, 'og', emork, ':')
print('Heildarkostnadur ferdar kvik bestun:', kostnadurKB0[hotelfjoldi])
print('Heildarkostnadur ferdar gradugt:', kostnadurGradugt0)
# print('Heildarkostnadur ferdar stoppa a ollum hotelum:', kostnadurStoppaOllumHotelum0[hotelfjoldi])
print()

# kostnadurEndurkvaemt = KostnadurEndurkvaemt(0,1)
# print('Heildarkostnadur ferdar endurkvaemt:', kostnadurEndurkvaemt)

'''''''''''''''  V1 - Önnur Gögn '''''''''''''''
exp = lambda a,b : random.expovariate(a/b)
mean                = 200
hotelfjoldi         = 100
stadafjoldi         = hotelfjoldi+1
hotel               = fDreifdHotel(1,mean,hotelfjoldi,exp)
hotelfjarlaegdir    = hotel[0]
hotelfylki          = hotel[1]
''''''''''''''''''''''''''''''''''''''''''''''''

kostnadurKB2 = KostnadurKB()
# kostnadurStoppaOllumHotelum2 = KostnadurStoppaOllumHotelum()
kostnadurGradugt2 = kostnadurGradugt()

print('Nidurstada med 100 hotel thar sem fjarlaegd a milli hotela er veldisdreifd slembitala med medaltal 200 :')
print('Heildarkostnadur ferdar kvik bestun:', kostnadurKB2[hotelfjoldi])
print('Heildarkostnadur ferdar gradugt:', kostnadurGradugt2)
# print('Heildarkostnadur ferdar stoppa a ollum hotelum:', kostnadurStoppaOllumHotelum2[hotelfjoldi])
print()