import math, random

class ListNode():
    
    def __init__(self, key, right, down=None):
        self.key = key
        self.right = right
        self.down = down


class SortedLinkedList():
    
    def __init__(self):
        self.tail = ListNode(math.inf, None)
        self.head = ListNode(-math.inf, self.tail)
        

class SkipList():

    def __init__(self):
        self.layers = 0
        self.sortedLists = [SortedLinkedList()]


    def contains(self, x):
        h = self.layers
        v = self.sortedLists[h].head
#        print('byrja leit á', x)
        while v is not None and v.key != x:
            if v.right.key > x:
#                a = str(v.down.key) if v.down is not None else 'None'
#                b = str(v.right.key) if v.right is not None else 'None'
#                print('fór niður úr hæð '+ str(h) + ' frá '+ str(v.key) + ' til ' + a + ' en til hægri er ' + b)
#                h-=1
                v = v.down
            else:
#                print('fór til hægri á hæð '+ str(h) + ' frá ' + str(v.key) + ' til ' + str(v.right.key))
                v = v.right
#            print()
        return v is not None and v.key == x


    def insert(self, x):
        h = self.layers
        L = self.sortedLists[h]
        v = L.head
        rVs = []
        while True: # Could put 'v.right.key == x' here instead of True
            if v.right.key < x:
                v = v.right
            elif v.down is not None:
                rVs.append(v)
                v = v.down
            elif v.right.key == x: # but fewer comparisons if kept here
                return
            else: # v.right.key > x and v.down is None. We are here!
                v.right = ListNode(x, v.right, v.down)
                self.updateAbove(x, rVs)
                break


    def updateAbove(self, x, rVs):
        i, n = 0, len(rVs)
        b = self.flipCoin() # flip coin
        while i < n and b: # add x to above layers
            rv = rVs[n-i-1]
            d = rv.down
            while x != d.key: # make sure x is pointing down to itself
                d = d.right
#            print(x, 'inserted with', d.key, 'below')
            rv.right = ListNode(x, rv.right, d)
            b = b and self.flipCoin()
            i+=1
        if i == n and b: # already added to top layer, add another?
            L = SortedLinkedList()
            L.head.down = self.sortedLists[self.layers].head
            L.tail.down = self.sortedLists[self.layers].tail
            self.layers += 1
            self.sortedLists.append(L)

    """ prentar hvern layer af listum L í SkipList á forminu:
        L[0].key (L[0].down.key) -> L[1] (L[1].down.key)...
    """
    def printSkipList(self):
        h = self.layers
        SL = self.sortedLists
        for i in range(h,-1,-1):
            L = SL[i]
            v = L.head
            l = ''
            d = ''
            while v is not None:
                d = str(v.down.key) if v.down is not None else ''
                l += str(v.key)  + ' (' + d + ') ' + '-> '
                v = v.right
            print(l)
        #    print(d)
            print()

    def flipCoin(self):
        return random.randint(0,1)==1

def main():
    skiplist = SkipList()
    
    
    for i in range(15):
        r = 2*i-1 # random.randint(0,100)
        skiplist.insert(r)
    
    skiplist.printSkipList()
    
    
    c=0
    for i in range(30):
        if not skiplist.contains(i):
            c+=1
    print(c)
