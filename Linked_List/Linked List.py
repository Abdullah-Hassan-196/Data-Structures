class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    class LinkedNode:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next

    def Append_Element(self,o):
        if self.head==None:
            self.head=self.LinkedNode(o)
            self.tail=self.head
        else:
            self.tail.next=self.LinkedNode(o)
            self.tail=self.tail.next
        self.count+=1

    def Print_List(self):
        current=self.head
        while current != None:
            print(current.data)
            current=current.next



    def Return_Index(self,value):
        i=1
        if self.head==None:
            raise Exception("Empty List")
        else:
            current=self.head
            while current!=None:
                if current.data==value:
                    return i
                else:
                    i+=1
                    current=current.next
        return -1



    def Pop(self):
        if self.head==None:
            raise Exception("Empty List")
        else:
            current=self.head
            self.head=current.next
            del(current.data)
        self.count-=1

    def is_empty(self):
        return self.count == 0


    def size(self):
        return self.count

    def Peek(self):
        if self.head==None:
            return False
        else:
            current=self.head
            return current.data

    def Peek_Last(self):
        if self.head==None:
            return False
        else:
            return self.tail.data



def main():
    L=LinkedList()
    L.Append_Element(10)
    L.Append_Element(50)
    L.Append_Element(1)
    L.Print_List()

    print("Index:", L.Return_Index(50))
    print()
    print(L.is_empty())
    print("Size: ",L.size())
    print(L.Peek())
    print(L.Peek_Last())

    L.Pop()
    L.Pop()
    L.Pop()
    print()
    print(L.is_empty())
    print(L.size())
    print(L.Peek())
main()
