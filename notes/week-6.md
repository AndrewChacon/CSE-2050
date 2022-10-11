# Week 6 - Recursion and Dynamic Programming

### Quick Recap - Linked Lists

Linear Data Structures

- Stacks, Queues -> using List [1, 2, 3, 4, ...] -> causes O(n)

### Node

```python
class _Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next
```

### Linked List

```python
class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = None
```

Insert element at the head

```python
self._head = _Node("Node Element", self._head)
```

Insert element at the tail

```python
newNode = _Node("Node Element", None)
self._tail._next = newNode
self._tail = newNode
```

Deleting element from the head

```python
self._head = self._head._next
```

Deleting element from the tail
No way of knowing the node proceeding at the tail node
List traversal would take `O(n)`

### Doubly Linked List

Nodes now contain a references for the next and previous nodes
We have `O(n)` operations for insert and delete at any postion in the list

next -> reference to the next node
prev -> reference to the previous node

```
 Header        Node         Node         Node        Trailer
  [  ]   <->   [  ]   <->   [  ]   <->   [  ]   <->   [  ]

"Header"  -> Head of the list
"Trailer" -> Tail of the list
```

#### Node

```python
class _Node:
    def __init__(self, prev, element, next):
        self._prev = prev
        self._element = element
        self._next = next
```

#### Doubly Linked List

```python
class DoublyLinkedBase():
    def __init__(self):
        self._header = _Node(None, None, None)
        self._trailer_ = _Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
```

**Insertion of a node**

Create a new node with reference of the predecessor and successor nodes
Then update `_next` and `_prev` pointers of predecessor and successor nodes to point to the new node

```python
def _insert_between(self, predecessor, element, successor):
    newest = _Node(predecessor, element, successor)
    predecessor._next = newest
    successor._prev = newst
    self._size = self._size + 1
    return newest
```

**Deletion of a node**

Link the neighbors of the nodes with each other
Set all the node values to none (optionally)

```python
def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next

    predecessor._next = successor
    successor._prev = predecessor
    self._size = self._size - 1

    element = node._element
    node._prev = node._next = node._element = None
    return element
```

## Recursion and Dynamic Programming

Recursion is a method of solving a problem with a help function
When the function **recursively** calls itself

Example: Adding K integers

```python
def sum(k):
    if k > 0:
        return sum(k - 1) + k
    return 0

print(sum(5)) -> 15
```

```
return 5 + sum(4)
return 5 + 4 + sum(3)
return 5 + 4 + 3 + (sum 2)
return 5 + 4 + 3 + 2 + sum(1)
return 5 + 4 + 3 + 2 + 1 + sum(0)
while k > 0 (condition has been met)

returns 15
```

A function can be made to call itself forever if not implemented correctly
Python has a built in RecursionError that prevents recusion going past 1000 iterations deep
When the limit is reached it will return an error
