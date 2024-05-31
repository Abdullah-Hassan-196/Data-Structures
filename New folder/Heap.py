class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_val

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        min_idx = idx

        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
            min_idx = right_child_idx

        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self._heapify_down(min_idx)

    def print_heap(self):
        print("Heap:", self.heap)


def main():
    heap = Heap()
    heap.insert(10)
    heap.insert(30)
    heap.insert(20)
    heap.insert(5)
    heap.insert(25)
    heap.insert(15)
    heap.print_heap()

    root_val = heap.delete()
    print("Root value removed:", root_val)
    heap.print_heap()
main()
