class Stack:
    def __init__(self):
        self.Stack = [None] * 50
        self.top = 0

    def Push(self, num):
        self.Stack[self.top] = num
        self.top += 1

    def Pop(self):
        if self.top == 0:
            print("Stack is empty")
            return None
        else:
            self.top -= 1
            element=self.Stack[self.top]
            return element

    def Peek(self):
        if self.top == 0:
            print("Stack is empty")
            return None
        else:
            return self.Stack[self.top - 1]

    def Is_Empty(self):
        return self.top == 0

    def Print(self):
        cur = self.top
        while cur != 0:
            print(self.Stack[cur - 1])
            cur -= 1

    def Size(self):
        return self.top


def main():
    s=Stack()
    s.Push(10)
    s.Push(20)
    s.Push(30)
    s.Push(40)
    s.Print()
    print()
    s.Pop()
    s.Pop()
    print(s.Is_Empty())
    print("Size: ",s.Size())
    print(s.Peek())

main()
