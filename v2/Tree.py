# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:20:35 2019

@author: Erling Oskar
"""

# Tvíleitartré
class Tree:

    # Smiður
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Innseting
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Uppfletting    
    def contains(self, key):
        if key < self.data:
            if self.left is None:
                return False
            return self.left.contains(key)
        elif key > self.data:
            if self.right is None:
                return False
            return self.right.contains(key)
        else:
            return True

    # Prenta tréið. Eyða fyrir skil
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Tree(12)
root.insert(6)
root.insert(14)
root.insert(3)
# print(root.contains(7))
# print(root.contains(14))

root.PrintTree()
root.contains(root.data)



"""
import random as random

class TreapNode():
    # Smiður
    def __init__(self, data, parent = None):
        self.data = data
        self.priority = random.random()
        self.parent = parent
        self.left = None
        self.right = None
        print('Node created')
#        self.balance()


class Treap():
    # Smiður
    def __init__(self):
        self.root = None

    # Uppfletting    
    def contains(self, data, r = None):
        if r is None:
            if self.root is None:
                print('leit: engin rot')
                return False
            r = self.root
        if data < r.data:
            if r.left is None:
                return False
            return self.contains(data, r.left)
        elif data > r.data:
            if r.right is None:
                return False
            return self.contains(data, r.right)
        else:
#           self.printNodeInfo()
            return True

    # innsetning
    def insert(self, data, r = None):
        if r is None:
            if self.root is None:
                self.root = TreapNode(data)
                return
            else:
                r = self.root
                print(r.data)
        if data < r.data:
            if r.left is None:
                r.left = TreapNode(data, r)
            else:
                self.insert(data, r.left)
        elif data > r.data:
            if r.right is None:
                r.right = TreapNode(data, r)
            else:
                self.insert(data, r.right)
        else: # data == r.data
            return

   
        
treap = Treap()
treap.contains(2)
treap.contains(3)
treap.insert(2)
treap.insert(3)

treap.insert(-4)

for i in range(10):
    treap.insert(i)    

for i in range(-5,15):
    print(str(i) + ' ' + str(treap.contains(i)))

"""