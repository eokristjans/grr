import random as random

class TreapNode():
    # Smiður
    def __init__(self, data, parent = None):
        self.data = data
        self.priority = random.random()
        self.parent = parent
        self.left = None
        self.right = None


class Treap():
    # Smiður
    def __init__(self):
        self.root = None

    # Uppfletting
    def contains(self, data):
        if self.root is None:
            return False
        self.__contains__(data, self.root)
    
    def __contains__(self, data, r):
        if data < r.data:
            if r.left is None:
                return False
            return self.__contains__(data, r.left)
        elif data > r.data:
            if r.right is None:
                return False
            return self.__contains__(data, r.right)
        else:
            return True

    # Innsetning
    def insert(self, data):
        if self.root is None:
            self.root = TreapNode(data)
            return
        self.__insert__(data, self.root)
        
    def __insert__(self, data, r):
        if data < r.data:
            if r.left is None:
                r.left = TreapNode(data, r)
                self.balance(r.left)
            else:
                self.__insert__(data, r.left)
        elif data > r.data:
            if r.right is None:
                r.right = TreapNode(data, r)
                self.balance(r.right)
            else:
                self.__insert__(data, r.right)
        else: # data == r.data
            return

    # laga hrúguskilyrði
    def balance(self, s):
        while s.parent is not None and s.priority < s.parent.priority:
            if s.data < s.parent.data:
                self.rotate_right(s)
            else: # self.data > self.parent.data
                self.rotate_left(s)
        if s.parent is None:
            self.root = s
         
    def rotate_right(self, s):
        p = s.parent
        g = p.parent
        if s.right is not None:
            s.right.parent = p
        if g is not None:
            if p is g.left:
                g.left = s
            else: # p is g.right
                g.right = s
        p.left = s.right
        s.parent = g
        p.parent = s
        s.right = p
                       
    def rotate_left(self, s):
        p = s.parent
        g = p.parent
        if s.left is not None:
            s.left.parent = p
        if g is not None:
            if p is g.left:
                g.left = s
            else: # p is g.right
                g.right = s
        p.right = s.left
        s.parent = g
        p.parent = s
        s.left = p
    
def main():
    treap = Treap()
    for i in range(-1000,1000):
        treap.insert(2*i)
    
    for i in range(-1001,1005):
        if not treap.contains(i):
            print(i)
            