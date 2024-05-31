class Unordered:

    def __init__(self, ARSize = 100):
        self.ARSize=ARSize
        self.ALSize=0
        self.Array=[None]*self.ARSize


    def isFull(self):
        return self.ALSize == self.ARSize

    def isEmpty(self):
        return self.ALSize == 0

    def size(self):
        return self.ALSize

    def append(self,o):
        if not self.isFull():
            self.Array[self.ALSize] = o
            self.ALSize = self.ALSize + 1

    def remove(self, index):
        if type(index) is self.UOIterator:
            index = index.current
        if index < 0 or index >= self.ALSize:
            raise Exception("Invalid Index")
        j = index
        while j < self.ALSize:
            self.Array[j] = self.Array[j+1]
            j = j + 1
        self.ALSize = self.ALSize - 1


    def set(self, index, o):
        if index>=0 and index<=self.ALSize:
            self.Array[index]=o

    def left(self, index):
        l = 2*index+1
        if l < self.ALSize:
            return l
        else:
            return self.ARSize #raise Exception("No left node")

    def right(self, index):
        r = 2*index+2
        if r < self.ALSize:
            return r
        else:
            return self.ARSize #raise Exception("No right node")

    def parent(self, index):
        p = int((index-1)/2)
        if p >= 0:
            return p
        else:
            return self.ARSize #raise Exception("No parent node")

    def Display(self):
        self.DisplayAux(0, 0)
        print()

    def DisplayAux(self, r, level):
        if r <= self.ALSize:
            print("    "*level, self.Array[r], sep="")
            self.DisplayAux(self.left(r), level+1)
            self.DisplayAux(self.right(r), level+1)

def main():
    # Create a new Doubly Linked List
    AL = Unordered()
    # Insert the element to empty list
    AL.append(10)
    # Insert the element at the end
    AL.append(20)
    AL.append(30)
    AL.append(70)
    AL.append(50)
    AL.append(60)
    AL.append(80)
    AL.append(90)
    AL.append(40)
    print("Displaying Data :")
    AL.Display()
    print(AL.isEmpty())
    print("Size: ",AL.size())
    print()
    AL.set(8,100)
    AL.set(1,200)
    print("Displaying Data :")
    AL.Display()

main()
