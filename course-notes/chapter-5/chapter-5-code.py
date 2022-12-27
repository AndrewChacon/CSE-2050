# Timing Programs

# Timing Programs - Example 1
def duplicates1(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i != j and L[i] == L[j]:
                return True
    return False

assert(duplicates1([1,2,6,3,4,5,6,7,8]))
assert(not duplicates1([1,2,3,4]))

import time

for i in range(5):
    n = 1000
    start = time.time()
    duplicates1(list(range(n)))
    timetaken = time.time() - start
    print("Time taken for n = ", n, ": ", timetaken)

# Timing Programs - Example 2

import time

def timetrials(func , n, trials = 10):
    totaltime = 0
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        totaltime += time.time() - start
    print("average =%10.7f for n = %d" % (totaltime/trials, n))

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates1, n)

# Timing Programs - Example 3

def duplicates2(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i):
            if L[i] == L[j]:
                return True
    return False

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates2, n)

# Timing Programs - Example 4
def duplicates3(L):
    n = len(L)
    return any(L[i] == L[j] for i in range(1, n) for j in range(i))

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates3, n)