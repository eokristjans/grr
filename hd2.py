
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

alist = [7,4,5,1,2,4,7,9]
mergeSort(alist)
print(alist)


# BASIC HASKELL ÚTGÁFA sem ég get endurskrifað: https://gist.github.com/morae/8494016 
