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


def main():
    root = Tree(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print(root.contains(7))
    print(root.contains(14))
    
    root.PrintTree()
    root.contains(root.data)
