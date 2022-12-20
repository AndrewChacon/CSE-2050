import unittest
from ADT import Stack_L, Queue_L, Stack_LL, Queue_LL

class TestStackL(unittest.TestCase):

    def test_init(self):
        s = Stack_L()

    def test_length(self):
        s = Stack_L()
        self.assertEqual(s.__len__(), 0)

    def test_isempty(self):
        s = Stack_L()
        self.assertEqual(s.isempty(), True)

    def test_peek(self):
        s = Stack_L()
        s.push(1)
        self.assertEqual(s.peek(), 1)

    def test_push(self):
        s = Stack_L()
        s.push(5)

    def test_pop(self):
        s = Stack_L()
        s.push(7)
        self.assertEqual(s.pop(), 7)


class TestQueueL(unittest.TestCase):

    def test_init(self):
        q = Queue_L()

    def test_length(self):
        q = Queue_L()
        self.assertEqual(q.__len__(), 0)

    def test_isempty(self):
        q = Queue_L()
        self.assertEqual(q.isempty(), True)

    def test_peek(self):
        q = Queue_L()
        q.enqueue(1)
        self.assertEqual(q.peek(), 1)

    def test_enqueue(self):
        q = Queue_L()
        q.enqueue(5)

    def test_dequeue(self):
        q = Queue_L()
        q.enqueue(7)
        self.assertEqual(q.dequeue(), 7)


class TestStackLL(unittest.TestCase):

    def test_init(self):
        s = Stack_LL()

    def test_length(self):
        s = Stack_LL()
        self.assertEqual(s._size, 0)

    def test_isempty(self):
        s = Stack_LL()
        self.assertEqual(s.is_empty(), True)

    def test_push(self):
        s = Stack_LL()
        s.push(10)

    def test_pop(self):
        s = Stack_LL()
        s.push(3)
        self.assertEqual(s.pop(), 3)

    def test_top(self):
        s = Stack_LL()
        s.push(5)
        self.assertEqual(s.top(), 5)


class TestQueueLL(unittest.TestCase):

    def test_init(self):
        q = Queue_LL()

    def test_length(self):
        q = Queue_LL()
        self.assertEqual(q._size, 0)

    def test_isempty(self):
        q = Queue_LL()
        self.assertEqual(q.is_empty(), True)

    def test_first(self):
        q = Queue_LL()
        q.enqueue(1)
        self.assertEqual(q.first(), 1)

    def test_enqueue(self):
        q = Queue_LL()
        q.enqueue(5)

    def test_dequeue(self):
        q = Queue_LL()
        q.enqueue(7)
        self.assertEqual(q.dequeue(), 7)

if (__name__ == '__main__'):
    unittest.main()
