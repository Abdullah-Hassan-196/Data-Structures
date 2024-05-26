class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None


    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node


    def peek_front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data


    def peek_back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


    def pop_front(self):
        if self.head == None:
            print("List is empty")

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            #temp.next = None
            return temp.data


    def pop_back(self):
        if self.tail == None:
            print("List is empty")

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            #temp.prev = None
            return temp.data


    def Print_List_From_Head(self):
        if self.head==None:
            raise Exception ("Empty List")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next

    def Print_List_From_Tail(self):
        if self.tail==None:
            raise Exception ("Empty List")
        else:
            temp=self.tail
            while temp!=None:
                print(temp.data)
                temp=temp.prev

    def remove(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                break
            node = node.next

    def add_before(self, data, new_data):
        node = self.head
        while node is not None:
            if node.data == data:
                new_node = self.Node(new_data)
                new_node.next = node
                new_node.prev = node.prev
                if node.prev is not None:
                    node.prev.next = new_node
                else:
                    self.head = new_node
                node.prev = new_node
                break
            node = node.next
    def add_after(self, data, new_data):
        node = self.head
        while node is not None:
            if node.data == data:
                new_node = self.Node(new_data)
                new_node.next = node.next
                new_node.prev = node
                if node.next is not None:
                    node.next.prev = new_node
                else:
                    self.tail = new_node
                node.next = new_node
                break
            node = node.next


def main():
    D=DoublyLinkedList()
    D.push_back(2)
    D.push_back(3)
    D.push_back(4)
    D.push_back(5)
    D.push_front(10)
    D.Print_List_From_Head()
    print()
    D.Print_List_From_Tail()
    print()

    print("Pop from Front: ",D.pop_front())
    print("Pop from Tail: ",D.pop_back())
    print(D.peek_front())
    print(D.peek_back())
main()
