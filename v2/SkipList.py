import math

class ListNode():
    
    def __init__(self, key, nextNode, nodeBeneath):
        self.key = key
        self.right = nextNode
        self.down = nodeBeneath


class SortedLinkedList():
    
    def __init__(self):
        self.tail = ListNode(math.inf, None)
        self.head = ListNode(-math.inf, self.tail)
        

class SkipList():

    def __init__(self):
        self.layers = 0
        self.skipLists = [SortedLinkedList()]


    def contains(self, x):
        v = self.skipLists[self.layers]
        while v is not None and v.key != x:
            if v.right.key > x:
                v = v.down
            else:
                v = v.right
        return v is not None and v.key == x
    

    def insert(self, x):
        v = self.skipLists[self.layers]
        
        

        
        while v.down is not None:
            if v.right.key < x:
                if v.down is None:
                    put(self, v, x)
                else: # put x here
                    v = v.down
            elif v.right.key != math.inf:
                v = v.right
            else: # 
                v = v.right
    
    
    
    def insert(self, x):
        h = self.layers
        L = self.skipLists
        currList = L[h]
        v = currList.head
        while v.next is not currList.tail and v.next.key < x:
            if v.next.key > x:
                h -= 1
                currList = L[h]
            elif v.next.key == x:
                return
            else:
                v = v.next    

 
"""""" 
    
        h = self.layers
        L = self.skipLists
        l = L[h]
        v = l.head
        terminator = L[h].tail
        while v is not terminator:
            if v.next is not None and v.next.key < x:
                v = v.next
                continue
            elif v.next is None:
                
            
        
        while L[h]:
            if v.next == math.inf:
                if h == 0: 
                    return False
                else:
                    h -= 1
            
            if v.next.key > x:
                h -= 1
                currList = L[h]
            elif v.next.key == x:
                return
            else:
                v = v.next