class Tree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.children = []
    def __init__(self):
        self.root = None
        self.size=0

    def addnode(self, n, p=None):
        if p == None and self.root == None:
            self.root = self.Node(n)
            self.size+=1
        elif p == None:
            raise Exception("Root Node already exist") #Typo Error, Task 1
        elif n != None and p != None:
            if self.root.data == p:
                self.root.children.append(self.Node(n))
                self.size+=1

            else:
                self.addnodeAux(self.root, n, p)

    def addnodeAux(self, r, n, p):
        for c in r.children:
            if c.data == p:
                c.children.append(self.Node(n))
                self.size+=1
                return
            self.addnodeAux(c, n, p)

    def Display(self):
        self.DisplayAux(self.root)
        print()

    def DisplayAux(self, r):
        if r != None:
            print(r.data)
            for c in r.children:
                self.DisplayAux(c)


    def Size(self):
        return self.size            #Task 2

    def leaves(self):               #Task 3
        return self.leavesAux(self.root)

    def leavesAux(self, r):
        if r is None:
            return 0
        elif len(r.children) == 0:
            return 1
        else:
            count = 0
            for c in r.children:
                count += self.leavesAux(c)
            return count


    def update(self, o, n):         #Task 4
        if self.root is None:
            raise Exception("Tree is empty")
        elif self.root.data == o:
            self.root.data = n
        else:
            self.updateAux(self.root, o, n)

    def updateAux(self, r, o, n):
        for c in r.children:
            if c.data == o:
                c.data = n
                return
            self.updateAux(c, o, n)
        raise Exception(f"Node with value {o} not found in tree")

    def level_wise(self):           #Task 5
        if self.root is None:
            return

        queue = [self.root]

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                print(node.data, end=' ')
                for child in node.children:
                    queue.append(child)
            print()

    def iterative_transversal_by_queue(self):
        if self.root == None:
            return
        q = [self.root]
        while len(q) > 0:
            cur = q[0]
            del q[0]
            for c in cur.children:
                q.append(c)
            print(cur.data, end = ' ')
        print()



    def depth(self, n):
        if self.root is None:
            return -1
        elif self.root.data == n:
            return 1
        else:
            return self.depthAux(self.root, n, 1)

    def depthAux(self, r, n, d):
        for c in r.children:
            if c.data == n:
                return d
            else:
                child_depth = self.depthAux(c, n, d+1)
                if child_depth != -1:
                    return child_depth
        return -1


def main():
    # Create a new tree
    t = Tree()
    # add the root element to the tree
    t.addnode(10)
    # add the element as child node to an existing node of tree
    t.addnode(30, 10)
    t.addnode(70, 10)
    t.addnode(2, 30)
    t.addnode(50, 30)
    t.addnode(60, 200)
    t.addnode(12, 70)


    # Display tree data
    print("Display tree data")
    t.Display()



    print("Size of tree:",t.Size())  #Task 2
    print()
    print("Size of leaves:",t.leaves()) #Task 3
    print()
    t.update(10,100)   #Task 4
    print("Display tree data after updating value")
    t.Display()
    print("Level_Wise: ")
    t.level_wise()     #Task 5
    print()
    print(t.depth(2)) #Task 6

main()
