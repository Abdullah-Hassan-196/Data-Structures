class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        left_child = self.left(i)
        right_child = self.right(i)
        smallest = i
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[i]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def peek_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def print_heap(self):
        print("Heap:", self.heap)


def main():
    heap = MinHeap()
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(10)
    heap.insert(5)
    heap.insert(82)
    heap.insert(9)
    heap.insert(7)
    heap.print_heap()
    print("Min element:", heap.extract_min())
    print("Min element:", heap.extract_min())
    print("Min element:", heap.extract_min())
    print("Min element:", heap.peek_min())
    heap.print_heap()
main()
