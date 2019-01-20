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
