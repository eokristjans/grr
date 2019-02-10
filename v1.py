# -*- coding: utf-8 -*-
"""
Namskeid:   Greining Reiknirita tol403
Kennari:    Hjalmtyr Hafsteinsson minnir mig ad hann se
Stofnun:    Haskoli Islands
Höfundur:   Erling Oskar Kristjansson
"""
import random
import numpy as np

# Hjalparfall
def FjarlaegdirMilliHotela():
    for i in range(1,stadafjoldi):
        print(fjarlaegd(i-1,i))
  
''''''''' Adferdir vid mat a kostnadi '''''''''
'''
Notar endurkvaemni til ad reikna minnsta kostnad 
vid ad ferdast fra hoteli numer ii til hotels jj
Hryllilega haegvirkt, ekki radlagt ad keyra
ef vidvaera breytan 'hotelfjoldi' > 25
'''

def KostnadurEndurkvaemt(ii,jj):
    kjj = kostnadur(fjarlaegd(ii,jj))
    if jj == hotelfjoldi:
        return kjj
    else:
        return min( KostnadurEndurkvaemt(ii,jj+1),
            kjj + KostnadurEndurkvaemt(jj,jj+1))

'''
Gradug adferd til ad reikna minnsta kostnad vid
ad ferdast fra hoteli numer 0 til hotels med
visinn 'hotelfjoldi'
'''
def KostnadurStoppaOllumHotelum():
    sumsofar = 0
    kostn = [0]
    for i in range(1,stadafjoldi):
        sumsofar += kostnadur(fjarlaegd(i-1,i))
        kostn.append(sumsofar)
    return kostn


''' Skilar fjarlaegd milli hotela numer i og j '''
fjarlaegd = lambda i,j : np.abs((hotelfylki[j] - hotelfylki[i]))
''' Skilar kostnadinum vid ad ferdast fjarlaegd x '''
kostnadur = lambda x : (200 - x)**2


## nn er heiltala, sidasta hotelid (=stadafjoldi)
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
    return minKostn  
            

'''''''''''''''  V1 - Gerd gagna  '''''''''''''''
def fDreifdHotel(aa,bb,nn,f):
    AA = [0]
    BB = []
    for i in range(nn):
        BB.append(f(aa,bb))
        AA.append(AA[i]+BB[i])
    return tuple(BB),tuple(AA)
    
unf = lambda a, b : random.uniform(a,b)
nmork, emork        = 100, 300
hotelfjoldi         = 100
stadafjoldi         = hotelfjoldi+1
hotel               = fDreifdHotel(nmork,emork,hotelfjoldi,unf)
hotelfjarlaegdir    = hotel[0]
hotelfylki          = hotel[1]
''''''''''''''''''''''''''''''''''''''''''''''''


kostnadurKB = KostnadurKB()
print('Heildarkostnadur ferdar kvik bestun:', kostnadurKB[hotelfjoldi])

kostnadurStoppaOllumHotelum = KostnadurStoppaOllumHotelum()
print('Heildarkostnadur ferdar _gradugt_:', kostnadurStoppaOllumHotelum[hotelfjoldi])

# kostnadurEndurkvaemt = KostnadurEndurkvaemt(0,1)
# print('Heildarkostnadur ferdar endurkvaemt:', kostnadurEndurkvaemt)


'''''''''''''''  V1 - Önnur Gögn '''''''''''''''
unf = lambda a, b : random.uniform(a,b)
nmork, emork        = 200, 201
hotelfjoldi         = 100
stadafjoldi         = hotelfjoldi+1
hotel               = fDreifdHotel(nmork,emork,hotelfjoldi,unf)
hotelfjarlaegdir    = hotel[0]
hotelfylki          = hotel[1]
''''''''''''''''''''''''''''''''''''''''''''''''

kostnadurKB = KostnadurKB()
print('Heildarkostnadur ferdar kvik bestun:', kostnadurKB[hotelfjoldi])

kostnadurStoppaOllumHotelum = KostnadurStoppaOllumHotelum()
print('Heildarkostnadur ferdar _gradugt_:', kostnadurStoppaOllumHotelum[hotelfjoldi])


'''''''''''''''  V1 - Önnur Gögn '''''''''''''''
exp = lambda a,b : random.expovariate(a/b)
mean                = 200
hotelfjoldi         = 100
stadafjoldi         = hotelfjoldi+1
hotel               = fDreifdHotel(1,mean,hotelfjoldi,exp)
hotelfjarlaegdir    = hotel[0]
hotelfylki          = hotel[1]
''''''''''''''''''''''''''''''''''''''''''''''''

kostnadurKB = KostnadurKB()
print('Heildarkostnadur ferdar kvik bestun:', kostnadurKB[hotelfjoldi])

kostnadurStoppaOllumHotelum = KostnadurStoppaOllumHotelum()
print('Heildarkostnadur ferdar _gradugt_:', kostnadurStoppaOllumHotelum[hotelfjoldi])
