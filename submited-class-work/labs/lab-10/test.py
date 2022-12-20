from PriorityQueue import Heap, Entry
import unittest

class TestHeapFunctions(unittest.TestCase):
    # test insert
    def testInsertFunction(self):
        heap = Heap()
        heap.insert("A", 13)
        item = heap._heap[0].item
        priority = heap._heap[0].priority
        self.assertEqual((item, priority) , ("A", 13))

    # test upheap
    def testUpheapFunction(self):
            heap = Heap()

            heap.insert("A", 13)

            item = heap._heap[0].item
            priority = heap._heap[0].priority
            self.assertEqual((item, priority) , ("A", 13))

            print('View Upheap Function')
            for entry in heap._heap:
                print(f"item: {entry.item}", end=" ")
                print(f"priority: {entry.priority}")
            print("")

            heap.insert("B", 2)
            item = heap._heap[0].item
            priority = heap._heap[0].priority
            self.assertEqual((item, priority) , ("B", 2))

            print('View Upheap Function')
            for entry in heap._heap:
                print(f"item: {entry.item}", end=" ")
                print(f"priority: {entry.priority}")
            print("")

            heap.insert("C", 0)
            item = heap._heap[0].item
            priority = heap._heap[0].priority
            self.assertEqual((item, priority) , ("C", 0))

            print('View Upheap Function')
            for entry in heap._heap:
                print(f"item: {entry.item}", end=" ")
                print(f"priority: {entry.priority}")
            print("")

    # test find min
    def testFindminFunction(self):
        heap = Heap()
        heap.insert("A", 13)
        heap.insert("B", 2)
        heap.insert("C", 0)
        heap.insert("D", 8)
        heap.insert("E", 1)
        heap.insert("F", 5)
        heap.insert("G", 25)
        self.assertEqual(heap.findmin(), ("C", 0))

        heap.removemin()
        self.assertEqual(heap.findmin(), ("E", 1))


    # test remove min
    def testRemoveminFunction(self):
        heap = Heap()
        heap.insert("A", 13)
        heap.insert("B", 2)
        heap.insert("C", 0)
        heap.insert("D", 8)
        heap.insert("E", 1)
        heap.insert("F", 5)
        heap.insert("G", 25)

        self.assertEqual(heap.removemin(), ("C", 0))
        self.assertEqual(heap.removemin(), ("E", 1))
        self.assertEqual(heap.removemin(), ("B", 2))

    # test downheap
    def testDownheapFunction(self):
        self.maxDiff = None
        heap = Heap()
        heap.insert("A", 13)
        heap.insert("B", 2)
        heap.insert("D", 8)
        heap.insert("F", 5)
        heap.insert("G", 25)

        heap._downheap(0)

        print("\nView Downheap Function")
        for entry in heap._heap:
            print(f"item: {entry.item}", end=" ")
            print(f"priority: {entry.priority}")
        print("")

        first_item = heap._heap[0].item
        first_priority = heap._heap[0].priority
        self.assertEqual((first_item, first_priority), heap.findmin())


unittest.main()

# heap = Heap()
# heap.insert("A", 13)
# heap.insert("B", 2)
# heap.insert("C", 0)
# heap.insert("D", 8)
# heap.insert("E", 1)
# heap.insert("F", 5)
# heap.insert("G", 25)

# print(f"min: {heap.findmin()}")
# heap.removemin()
# heap.removemin()
# for entry in heap._heap:
#     print(f"item: {entry.item}", end=" ")
#     print(f"priority: {entry.priority}")