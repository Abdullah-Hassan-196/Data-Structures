class ArrayList:
    def __init__(self, ARSize = 100):
        self.ARSize=ARSize
        self.ALSize=0
        self.Array=[None]*self.ARSize


    def append(self,o):
        if not self.isFull():
            self.Array[self.ALSize] = o
            self.ALSize = self.ALSize + 1

    def pop(self):
        ele=self.Array[self.ALSize]
        self.ALSize-=1
        #del ele

    def POP_FULL(self):
        j = 0
        while self.ALSize>j:
            del self.Array[j]
            self.ALSize-=1
            self.ARSize-=1

    def Display(self):
        j = 0
        while j < self.ALSize:
            print(self.Array[j])
            j = j + 1
        print()


    def set(self, old, val):
        index=self.Array.index(old)
        self.Array[index]=val

    def Remove(self,val):
        index=self.Array.index(val)
        del(self.Array[index])
        self.ALSize-=1


    def size(self):
        return self.ALSize

    def isEmpty(self):
        return self.ALSize == 0

    def isFull(self):
        return self.ALSize == self.ARSize




def main():
    AL = ArrayList()
    # Insert the element to empty list
    AL.append(10)
    # Insert the element at the end
    AL.append(20)
    AL.append(30)
    AL.append(69)
    AL.append(70)
    AL.append(50)
    AL.append(60)
    AL.append(80)
    AL.append(90)
    AL.append(40)
    print("Display 10 items")
    AL.Display()
    AL.pop()
    AL.set(50,100)
    AL.Display()

    AL.Remove(20)
    AL.Display()
    print("Size: ",AL.size())
    AL.POP_FULL()
    print("Size: ",AL.size())

main()

