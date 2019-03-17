# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:28:41 2019

@author: Erling Oskar
"""
import random

class SkipNode:
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        self.next = [None]*height
        
class SkipList:
    def __init__(self):
        self.head = SkipNode()
        
    
    def updateList(self, elem):
        update = [None]*len(self.head.next)
        x = self.head
        for i in reversed(range(len(self.head.next))):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update
    
    
    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None


    def insert(self, elem):
     
        node = SkipNode(self.randomHeight(), elem)  """ randomHeight()?? """
     
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)
     
        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node


skiplist = SkipList()
for i in range(10):
    skiplist.insert(i)

for i in range(-5,15):
    print(skiplist.find(i))