from Node import _Node

class Stack_L:
    def __init__(self):
        self._L = list()

    def push(self, item):
        self._L.append(item)

    def pop(self):
        """ Remove element from the top of the stack """
        if self.isempty():
            raise Exception("Your trying to pop an empty stack")
        return self._L.pop()

    def peek(self):
        if self.isempty():
            raise Exception("Your trying to peek an empty stack")
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

class Queue_L:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        if self.isempty():
            raise Exception("Your trying to deque from the empty queue")
        return self._L.pop(0)

    def peek(self):
        return self._L[0]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

class Stack_LL:
    def __init__(self):
        self._head = None
        self._size = 0
        self._LL = []

    def __len__(self):
        """ Returns the size of the stack """
        return self._size

    def is_empty(self):
        """ Returns True if the stack is empty"""
        if self._size == 0:
            return True
        else:
            return False

    def push(self, element):
        """ Add "element" to the top of the stack """
        self._size = self._size + 1
        self._head = _Node(element, self._head)

    def pop(self):
        self._size = self._size - 1
        currentHead = self._head._element
        self._head = self._head._next
        return currentHead

    def top(self):
        """ Only read the element and donot remove it. """
        if self.is_empty():
            raise Exception("Your trying to peek an empty stack")
        return self._head._element

class Queue_LL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the size of the queue """
        return self._size

    def is_empty(self):
        """ Returns True if the queue is empty"""
        if self._size == 0:
            return True
        else:
            return False

    def first(self):
        """ Returns (but do not remove) the first element in the queue """
        if self.is_empty():
            raise Exception("Your trying to peek an empty queue")
        return self._head._element

    def enqueue(self, element):
        """ Add "element" to the back of the queue """
        self._size = self._size + 1
        if self._head is None:
            self._head = _Node(element, self._head)
            if self._tail is None:
                self._tail = self._head
        else: 
            self._tail._next = _Node(element, None)
            self._tail = self._tail._next

    def dequeue(self):
        """ Remove element from the front of the queue """
        if self.is_empty():
            raise Exception("Your trying to dequeue an empty queue")
        self._size = self._size - 1
        item = self._head._element
        self._head = self._head._next
        if self._head is None: self._tail = None
        return item




stack = Stack_L()
for i in range(1, 11):
    stack.push(i)

queue = Queue_L()
for i in range(1, 11):
    stack.push(i)
# print(stack.isempty())
# print(stack.pop())