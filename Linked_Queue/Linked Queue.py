from abc import ABC, abstractmethod


class Queue(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self, item):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass


class LinkedQueue(Queue):
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next


    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        if self.head == None:
            self.head = self.Node(item)
            self.tail = self.head
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next
        self.count += 1

    def dequeue(self):
        if self.head == None:
            raise Exception("Queue is empty")
        else:
            tmp = self.head
            self.head = self.head.next
            self.count -= 1
            return tmp.data

    def is_empty(self):
        return self.count == 0


    def size(self):
        return self.count

    def Print_Queue(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next
        print()

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
    L=LinkedQueue()
    L.enqueue(100)
    L.enqueue(200)
    L.enqueue(50)
    L.enqueue(150)
    L.enqueue(10)
    L.enqueue(30)

    L.Print_Queue()
    print("Size :",L.size())

    print(L.Peek())
    print(L.Peek_Last())


    L.dequeue()
    L.dequeue()

    print(L.is_empty())
    L.Print_Queue()
    print("Size :",L.size())
main()
