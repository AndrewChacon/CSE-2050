# def f(k):
#     if k > 0:
#         return f(k-1) + k
#     return 0

# print(f(5))


# def f(k):
#     var = k * 2
#     return g(k+1) + var

# def g(k):
#     var = k + 1
#     return var + 1


# print(f(15))


# def a(k):
#     if k == 0: return 0
#     return b(k)

# def b(k):
#     return c(k)

# def c(k):
#     return a(k-1)

# print(a(340))
# RecursionError: maximum recursion depth exceeded


# def fib(k):
#     if k in [0,1]: return k
#     return fib(k-1) + fib(k-2)

# print([fib(i) for i in range(15)])

# def fib(k):
#     a, b = 0, 1
#     for i in range(k):
#         a, b = b, a + b
#     return a

# print(fib(400))



# RECURSIVE APPROACH

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)


# ITERATIVE APPROACH

def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial

# print(get_recursive_factorial(5))
# print(get_iterative_factorial(6))


# Fibonacci Sequence
def fib(k):
    if k in [0, 1]:
        return k
    return fib(k-1) + fib(k-2)


# Fibonacci Sequence Using Memoization
def fib_memo(k, fib_array):
    if k in [0,1]:
        fib_array[k] = k
        return fib_array[k]
    if fib_array[k] != None:
        return fib_array[k]
    fib_array[k] = fib_memo(k-1, fib_array) + fib_memo(k-2, fib_array)
    return fib_array[k]

k = 10
fib_array = [None] * (k+1)

print(fib(10))
print(fib_memo(k, fib_array))

def fib_dyn(k):
    if k <= 1:
        return k
    F = [0, 1]

    for i in range(2, k+1, 1):
        F.append(F[i-1] + F[i-2])
    return F[k]

print(fib_dyn(10))