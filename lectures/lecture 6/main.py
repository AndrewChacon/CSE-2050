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

def fib(k):
    a, b = 0, 1
    for i in range(k):
        a, b = b, a + b
    return a

print(fib(400))