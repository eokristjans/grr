########## GrR Heimadæmi 4 ##########
##### HD4.3 Hjálparfall, skilar afriti af listanum L
def copyList(L):
    cL = []
    for l in L:
        cL.append(l)
    return cL

##### HD4.3b
# Notkun:   maxWeight = WeightOfSubsetSums(X,W,T,wsf,k,w)
# Fyrir:    X[1..n], W[1..n] eru heiltölulistar
#           T (jákvæð), wsf eru heiltölur
#           k=[0], w=[float('-inf')] í upphafi
# Eftir:    X og W haldast hönd í hönd.
#           maxWeight er hæsta summa þeirra talna í W[j]
#           þar sem sum(X[i])=T
#   maxWeight=float('-inf') ef ekkert undirmengi X hefur summuna T
def WeightOfSubsetSums(X,W,T,wsf,k,w):
    if T == 0:
        w.append(wsf)
        k[0] += 1
    elif T<0 or len(X)==0:
        return
    else:
        Xn = X.pop()
        Wn = W.pop()
        print(Wn)
        cX1 = copyList(X)
        cX2 = copyList(X)
        cW1 = copyList(W)
        cW2 = copyList(W)
        WeightOfSubsetSums(cX1,cW1,T-Xn,wsf+Wn,k,w)
        WeightOfSubsetSums(cX2,cW2,T,wsf,k,w)
    return max(w)

k = [0]
w = [float('-inf')]
A = [1,3,4]
W = [1,1,1]
maxWeight = WeightOfSubsetSums(A,W,4,0,k,w)
print(maxWeight) #$ 2

##### GrR HD4.3a
# Notkun:   a = NumberOfSubsetSums(X,T,k):
# Fyrir:    X[1..n] er heiltölulisti, T er jákvæð heiltala
#           k=[0] í upphafi
# Eftir:    a er fjöldi undirmengja talnanna úr X sem hafa mengjasummuna T
def NumberOfSubsetSums(X,T,k):
    if T == 0:
        k[0] += 1
    elif T<0 or len(X)==0:
        return
    else:
        Xn = X.pop()
        cX1 = copyList(X)
        cX2 = copyList(X)
        NumberOfSubsetSums(cX1,T-Xn,k)
        NumberOfSubsetSums(cX2,T,k)
    return k[0]



########## GrR Heimadæmi 3 ##########
# Hd3.4
# Notkun:   b = h3d3(A)
# Fyrir:    A er listi af lengd n
# Gildi:    b er True ef A inniheldur meira en n/4 eins stök
#           b er því ávalt True ef n < 4
def h3d3(A):
    b0 = False
    n = len(A)
    m = n/4
    print("A er", A)
    print("Lengd A er", n)
    print("Þurfum meira en", m, "eins stök") 
    BE = [None,None,None]
    BC = [0,0,0]
    # Tími O(9n)
    for a in A:
        # b er satt ef ekki búið að gera neitt við a
        b = True
        # Gættum gert: if None in BC
        # Hækka teljara staksins ef það er í BE. Tími O(3)
        # hér er jafngilt/betra: if a in BC
        for i in range(3):
            if BE[i] == a:
                BC[i] += 1
                b = False
                break
        if b: # hér er jafngilt/betra: elif 0 in BC
        # Setja a í BE ef það er laust pláss. Tími O(3)
            for i in range(3):
                if BC[i] == 0:
                    BE[i] = a
                    BC[i] = 1
                    b = False
                    break
        if b:
        # Ef a hvorki í BE né laust pláss:
            for j in range(3):
                BC[j] -= 1
    # Teljum raunverulegan fjölda hvers mögulegs staks, timi O(3n)
    for e in BE:
        count = 0
        for a in A:
            if e == a:
                count += 1
        b0 = count > m
        if b0:
            print("A inniheldur", count, "eintök af stakinu", e)
            return b0
    print("A inniheldur ekki meira en", m, "eintök af neinu staki") 
    return b0
    
A = [[1],[1,2],[1,2,3],[1,2,3,4],
    ['a','b'],['string','strong','strung','strong'],
    [1,2,3,4,7,6,5,4,4]]
for a in A:
    h3d3(a)
    print()

    

# Hd3.5
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


# Hd3.5
# falling(n,m) = n!/(n-m)!
# falling(n,n) = n!/(n-n)! = n!
def falling(n,m):
    if m==0:
        return 1
    elif m==1:
        return n
    else:
        mfloor = m//2
        mceiling = mfloor+m%2
        return falling(n,mfloor)*falling(n-mfloor,mceiling)

# Hd3.5a
# Fyrir:    f er fall sem tekur eitt viðfang
#           g er fall sem tekur tvö viðföng
#           k er tala sem föllin f og g ráða við
# Gildi:    Ber saman útkomurnar úr f og g fyrir tölur frá 0 upp í k
#           Prentar niðurstöður
def compareFunctions(f,g,k):
    for i in range(k):
        try:
            a = f(i)
            b = g(i,i)
            if a != b:
                print(a, " ", b)
                print("Virkar ekki fyrir heiltöluna: ", i)
                break
        except RecursionError as re:
            print("Annað fallið ræður ekki við heiltölur stærri en ", i)
            print("Hættir keyrslu")
            break
    print("Föllin gefa sömu niðurstöðu fyrir allar jákvæðar heiltölur minni en ", i)

#Hd3.5a
compareFunctions(factorial,falling,10000)
# Annað fallið ræður ekki við heiltölur stærri en  2960
# Hættir keyrslu
# Föllin gefa sömu niðurstöðu fyrir allar jákvæðar heiltölur minni en  2960



def print_hanoi(Peg,n):
    if n % 2 == 0:
        print("n", Peg[0], "n", Peg[2], "n", Peg[1])
    else:
        print()
        for p in Peg:
            print(p)

def move_hanoi(Peg,imod3):
    if imod3 == 0:
        if Peg[1] != []: 
            if Peg[2] == [] or Peg[1][0] < Peg[2][0]:
                Peg[2].append(Peg[1].pop())
                return True
        elif Peg[2] != []: 
            if Peg[1] == [] or Peg[2][0] < Peg[1][0]:
                Peg[1].append(Peg[2].pop())
                return True
        else:
            return False
    elif imod3 == 1:
        if Peg[0] != []:
            if Peg[2] == [] or Peg[0][0] < Peg[2][0]:
                Peg[2].append(Peg[0].pop())
                return True
        elif Peg[2] != []:
            if Peg[0] == [] or Peg[2][0] < Peg[0][0]:
                Peg[0].append(Peg[2].pop())
                return True
        else:
            return False
    elif imod3 == 2:
        if Peg[1] != []:
            if Peg[0] == [] or Peg[1][0] < Peg[0][0]:
                Peg[0].append(Peg[1].pop())
                return True
        elif Peg[0] != []:
            if Peg[1] == [] or Peg[0][0] < Peg[1][0]:
                Peg[1].append(Peg[0].pop())
                return True
        else:
            return False

def hanoi(n):
    i = 1
    Peg = [[], [], []]
    if n % 2 == 0:
        Peg[1], Peg[2] = Peg[2], Peg[1]
    for k in range(n,0,-1):
        Peg[0].append(k)
    b = True
    
    while b and i<9:
        print_hanoi(Peg,n)
        b = move_hanoi(Peg, i%3)
        print("i : ", i)
        i += 1
    

hanoi(3)


    for n in range(100):
        i = (2**n - 1) % 3
        print("n: ", n, ", i: ", i)


    ''' Úr move_hanoi tilraun
    if im3 == 0:
        if Peg[0] != []:
            if Peg[1] == [] or Peg[0][0] < Peg[1][0]:
                Peg[1].append(Peg[0].pop())
            elif Peg[2] == [] or Peg[0][0] < Peg[2][0]:
                Peg[2].append(Peg[0].pop())
        elif Peg[1] != []: 
            if Peg[2] == [] or Peg[1][0] < Peg[2][0]:
                Peg[2].append(Peg[1].pop())
        elif Peg[2] != []: 
            if Peg[1] == [] or Peg[2][0] < Peg[1][0]:
                Peg[1].append(Peg[2].pop())
        else:
            return False
    elif im3 == 1:
        if Peg[1] != []:
            if Peg[2] == [] or Peg[1][0] < Peg[2][0]:
                Peg[2].append(Peg[1].pop())
            elif Peg[0] == [] or Peg[1][0] < Peg[0][0]:
                Peg[0].append(Peg[1].pop())
        elif Peg[0] != []:
            if Peg[2] == [] or Peg[0][0] < Peg[2][0]:
                Peg[2].append(Peg[0].pop())
        elif Peg[2] != []:
            if Peg[0] == [] or Peg[2][0] < Peg[0][0]:
                Peg[0].append(Peg[2].pop())
        else:
            return False
    elif im3 == 2:
        if Peg[2] != []:
            if Peg[0] == [] or Peg[2][0] < Peg[0][0]:
                Peg[0].append(Peg[2].pop())
            elif Peg[1] == [] or Peg[2][0] < Peg[1][0]:
                Peg[1].append(Peg[2].pop())
        if Peg[1] != []:
            if Peg[0] == [] or Peg[1][0] < Peg[0][0]:
                Peg[0].append(Peg[1].pop())
        elif Peg[0] != []:
            if Peg[1] == [] or Peg[0][0] < Peg[1][0]:
                Peg[1].append(Peg[0].pop())
        else:
            return False
    return True
    '''

### Önnur útfærlsa sem virkar
def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)
       merge(alist,lefthalf,righthalf)


def merge(alist, lefthalf, righthalf):
    i=0
    j=0
    k=0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k]=lefthalf[i]
            i=i+1
        else:
            alist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        alist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        alist[k]=righthalf[j]
        j=j+1
        k=k+1

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


# BASIC HASKELL ÚTGÁFA sem ég get endurskrifað: https://gist.github.com/morae/8494016 
