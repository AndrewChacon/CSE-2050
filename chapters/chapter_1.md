# Overview

Sequence: Performing operations one at a time in a specific order.
Selection: Using conditional statements such as if to select which operations to execute.
Iteration: Repeating some operations using loops or recursion.

The process of moving from thinking about code to writing code.

Python can do simple arithmetic expressions: `print(1 + 1)`
We can also do comparison expressions like `5 > 7`
Here is an example of a more complicated expression:

```python
5 * (3 + abs(-12) / 3)
```

We store information in variables, the equal sign is the assignment operator

```python
variable_name = some_value
```

Similar operations include: `+=, -=, *=, /=`
An example of this `x += 1` is equivilant to `x = x + 1`

Every variable is associated with some piece of data, each of these objects has a type associated with it as well
integers, floats, booleans

```python
x = 5
y = 3.2
z = True
```

Strings are a sequence of characters and be used to store text

```python
s = "Hello"
t = "World"
u = s + t
print(u) -> 'HelloWorld'
```

Lists are ordered sequences of objects

```python
L = [1, 2, 3, 4, 5, 6]

print(L[0]) -> 1
print(L[2]) -> 3
print(L[4]) -> 5
print(L[-1]) -> 6

L[0] = 1
```

Tuples are also ordered sequences of objects, they are immutable

```python
t = (1, 2, "skip a few", 99, 100)
```

Dictonaries store key value pairs, if you have the key you can get the value. Also known as maps, mappings or hash tables.
Does not have a fixed order

```python
d = dict()
d[5] = 'five'
d[2] = 'two'
d['pi'] = 3.1315926
```

Sets are a collection of objects without duplicates, also has no fixed ordering. We can say that it is a nonsequential collection.

```python
s = {2, 1}
s.add(3)
s.add(2)
s.add(2)
s.add(2)

print(s) -> {1, 2, 3}

set() -> how to write an empty set
```

Other forms of control flow

```python
if False:
    print("this is bad")
else:
    print("this will print")
```

```python
x = 1
while x < 128:
    print(x, end=' ')
    x = x * 2

-> 1 2 4 8 16 32 64
```
