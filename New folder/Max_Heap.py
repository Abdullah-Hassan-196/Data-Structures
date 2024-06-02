class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        max_idx = idx

        if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[max_idx]:
            max_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[max_idx]:
            max_idx = right_child_idx

        if max_idx != idx:
            self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
            self._heapify_down(max_idx)

    def print_heap(self):
        print("Max Heap:", self.heap)

def main():
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(30)
    heap.insert(20)
    heap.insert(5)
    heap.insert(25)
    heap.insert(15)
    heap.insert(0)

    heap.insert(15)
    heap.print_heap()

    print("Max value removed:", heap.delete_max())
    print("Max value removed:", heap.delete_max())
    print("Max value removed:", heap.delete_max())

    heap.print_heap()
main()
