class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class Heap:
    def __init__(self):
        self._heap = []

    def insert(self, item, priority):
        self._heap.append(Entry(item, priority))
        self._upheap(len(self._heap) - 1)

    def _upheap(self, i):
        parent = (i - 1) // 2
        if i > 0 and self._heap[i] < self._heap[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _swap(self, c, p):
        self._heap[c], self._heap[p] = self._heap[p], self._heap[c]

    def findmin(self):
        return self._heap[0].item

    def removemin(self):
        item = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._downheap(0)
        return item

    def _downheap(self, p_idx):
        L = self._heap
        left = self._left(p_idx)
        right = self._right(p_idx)
        index = p_idx

        if self._has_left_child(p_idx) and self._heap[index] > self._heap[left]:
            index = left
        if self._has_right_child(p_idx) and self._heap[index] > self._heap[right]:
            index = right
        if index != p_idx:
            self._swap(p_idx, index)
            self._downheap(index)

    def _has_left_child(self, i):
        return self._left(i) < len(self._heap)

    def _has_right_child(self, i):
        return self._right(i) < len(self._heap)

    def _parent(self, i):
        return (i - 1)//2

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

if __name__ == '__main__':

    heap = Heap()
    heap.insert("A", 13)
    heap.insert("B", 2)
    heap.insert("C", 0)
    heap.insert("D", 8)
    heap.insert("E", 1)
    heap.insert("F", 5)
    heap.insert("G", 25)

    print(f"min: {heap.findmin()}")
    heap.removemin()
    heap.removemin()
    for entry in heap._heap:
        print(f"item: {entry.item}", end=" ")
        print(f"priority: {entry.priority}")
