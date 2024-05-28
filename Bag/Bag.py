class Bag:
    def __init__(self):
        self.items = []
        self.count=0

    def insert(self, item):
        self.items.append(item)
        self.count+=1
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self.count-=1
    def set(self, old_item, new_item):
        index = self.items.index(old_item)
        self.items[index] = new_item

    def size(self):
        return (self.count)

    def is_empty(self):
        return self.count == 0

    def search(self, item):
        if item in self.items:
            return True
        return False

    def iterate(self):
        for item in self.items:
            print (item)

    def join(self, other_bag):
        new_bag = Bag()
        for item in self.items:
            new_bag.insert(item)
        for item in other_bag.items:
            new_bag.insert(item)
        return new_bag

    def split(self, condition):
        left_bag = Bag()
        right_bag = Bag()
        for item in self.items:
            if condition(item):
                left_bag.insert(item)
            else:
                right_bag.insert(item)
        return (left_bag, right_bag)

    def clone(self):
        new_bag = Bag()
        for item in self.items:
            new_bag.insert(item)
        return new_bag

    def clear(self):
        self.items.clear()


def main():
    b=Bag()
    b.insert(10)
    b.insert(20)
    b.insert(30)
    b.set(10,100)
    b.iterate()
    print()
    print(b.is_empty())
    print()
    print("Size: ",b.size())
    print(b.search(100))
    print()

    b2=Bag()
    b2.insert(50)
    b2.insert(60)
    b2.insert(70)
    b2.iterate()
    print(b.join(b2))

    b3=Bag()
    print(b3.clone())
main()
