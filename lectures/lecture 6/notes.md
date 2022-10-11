# Chapter 9 - Recursion

You can think of Recursion as the process of a function repeating again and again until some base function is satisfied. When it repeats it'll use the values from the previous function call in the next sequence.
It will run until a base condition is met, consists of 2 components

1. **Base Condition** - In order to stop a recursive function we need a base condition. If it is missing it can result in an infinite loop
2. **Recursive Step** - It divides a big problem into smaller instances that are solved by the recursive function and later on gets recombined in the result

**Our objective**

1. Understand how recursion is used in a computer and translate it into a model or how to think of recursive functions

2. Use recursion as a method of problem solving, recognize the best times to use it

3. Be able to analyze the runtime of a function

**Example of a recursive function**

```python
def f(k):
    if k > 0:
        return f(k-1) + k
    return 0

print(f(5))
```

This is similar to the sumk function
To find the sum of numbers from 1 to K, it finds the sum of numbers from 1 to K-1, and then adds K

### Some Basics

Our recursive function should be moving towards the base case so we get a termination

Inorder to prevent infinite recursion loop python has a built in **RecursionError** to stop a stack overflow. The maximum depth by default is a recursive function cannot exceed a maximum depth of 1000

### The Function Call Stack

An idea of how recursion works on a computer.
There is no difference in making a recursive function call compared to other function calls

```python
def f(k):
    var = k * 2
    return g(k+1) + var

def g(k):
    var = k + 1
    return var + 1


print(f(15))

15
```

This example gives a **RecursionError**, this error is telling us that the call stack has reached its limit

```python
def a(k):
    if k == 0: return 0
    return b(k)

def b(k):
    return c(k)

def c(k):
    return a(k-1)

print(a(340))
```

### The Fibonacci Sequence

A classic recursivly defined function, originally created to predict the growth of rabbit populations

```python
def fib(k):
    if k in [0, 1]: return k
    return fib(k-1) + fib(k+2)

print([fib(i) for i in range(15)])
```

### Euclids Algorithm

```python
def fib(k):
    a, b = 0, 1
    for i in range(k):
        a, b = b, a + b
    return a

print(fib(400))
```
