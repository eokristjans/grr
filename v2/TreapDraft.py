
class TreapNode():
    # Smiður
    def __init__(self, data, parent = None):
        self.data = data
        self.priority = random.random()
        self.parent = parent
        self.left = None
        self.right = None
        self.balance()

# Hrúgutré
class Treap():
    
    # Smiður
    def __init__(self, data, parent = None):
        self.data = data
        self.priority = random.random()
        print(self.priority)
        self.parent = parent
        self.left = None
        self.right = None
        self.balance()

    def printNodeInfo(self):
        print('Treap Info:')
        a = 'self... data: ' + str(self.data) + ', prio: ' + str(self.priority)
        print(a)
        if self.parent != None:
            b = 'self.parent... data: ' + str(self.parent.data) + ', prio: ' + str(self.parent.priority)
            print(b)
        else:
            b = 'self.parent... None'
            print(b)
        if self.left != None:
            l = 'self.left... data: ' + str(self.left.data) + ', prio: ' + str(self.left.priority)
            print(l)
        if self.right != None:
            r = 'self.right... data: ' + str(self.right.data) + ', prio: ' + str(self.right.priority)
            print(r)
        print()

    # Uppfletting    
    def contains(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.contains(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.contains(data)
        else:
            self.printNodeInfo()
            return True

    # Innseting
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Treap(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Treap(data, self)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def swap_parents(self):
        s = self
        p = self.parent
        if p.parent != None:
            g = p.parent
            if p.data < g.data:
                g.left = s
            else: 
                g.right = s
            s.parent = g
        else:
            s.parent = None

    def rotate_right(self):
        print('snúum til hægri um ' + str(self.data))
        s = self
        temp = s.right
        p = self.parent
        self.swap_parents()
        if temp != None:
            p.left = s.right
            p.left.parent = p
        p.parent = s
        
    def rotate_left(self):
        print('snúum til vinstri um ' + str(self.data))
        s = self
        temp = s.left
        p = self.parent
        self.swap_parents()
        if temp != None:
            p.right = temp # mism lína 1
            p.right.parent = p # mism lína 2
        p.parent = s

    def balance(self):
        while self.parent != None and self.priority < self.parent.priority:
            if self.data < self.parent.data:
                self.rotate_right()
            else: # self.data > self.parent.data
                self.rotate_left()

    # Prenta tréið. Eyða fyrir skil
    def PrintTree(self):
        print(str(self.data) + ' : ' + str(self.priority))
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
    
    

treap = Treap(2)

treap.insert(3)
treap.PrintTree()

treap.insert(4)
treap.PrintTree()


for i in range(5):
    print(i)
    treap.insert(i) 
    treap.PrintTree()
    print()

print(treap.contains(1))

treap.PrintTree()
