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


class Array_Queue(Queue):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.arr = [0] * 100000

    def enqueue(self, data):
        if self.head == None:
            self.arr[0] = data
            self.head = self.arr[0]
            self.tail = self.arr[0]
            self.size += 1
        else:
            self.arr[self.size] = data
            self.tail = self.arr[self.size]
            self.size += 1

    def dequeue(self):
        if self.head == None:
            raise "Nothing to Dequeue"
        self.size -= 1
        self.head = self.head.next

    def peek(self):
        return self.tail

    def reverse_sort_2D_array(self):
        i = 0
        while i < self.size:
            j = 0
            while j < self.size-1:
                if self.arr[j][1] < self.arr[j+1][1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                j += 1
            i += 1

        return self.arr[0:self.size]
