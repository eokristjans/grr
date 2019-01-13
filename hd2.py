def merge_sort(A):
    n = len(A)
    if n > 1:
        m = n // 2
        L = A[:m]
        R = A[m:]
        merge_sort(L)
        merge_sort(R)
        merge(L,R,A)

# ekki endurkvæmt
def merge(L,R,A):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]: 
            A[k] = L[i] 
            i+=1
        else: 
            A[k] = R[j] 
            j+=1
        k+=1
        
        while i < len(L): 
            A[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            A[k] = R[j] 
            j+=1
            k+=1


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
