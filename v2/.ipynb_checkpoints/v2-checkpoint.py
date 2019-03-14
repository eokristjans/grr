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
    def lookup(self, key):
        if key < self.data:
            if self.left is None:
                return str(key)+" fannst ekki" # False
            return self.left.lookup(key)
        elif key > self.data:
            if self.right is None:
                return str(key)+" fannst ekki" # False
            return self.right.lookup(key)
        else:
            print(str(self.data) + ' fannst') # True

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
# print(root.lookup(7))
# print(root.lookup(14))

for i in range(100):
    root.insert(random.randint(1,70))

root.PrintTree()
root.lookup(root.data)


import random as random
# Hrúgutré
class Treap(Tree):
    
    # Smiður
    def __init__(self, data, priority=random.random()):
        super().__init__(data)
        self.priority = priority
    
    def insert(self,data):
        

        
treap = Treap(5)
print(treapRoot.lookup(5))