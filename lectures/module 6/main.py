# BINARY SEARCH

def binary_search(L, item):
    if len(L) == 0:
        return False
    mid_index = len(L) // 2
    if item == L[mid_index]:
        return True
    elif item < L[mid_index]:
        return binary_search(L[ : mid_index], item)
    else:
        return binary_search(L[mid_index + 1 : ], item)


def binary_search_improved(L, item, lower, upper):
    if lower < upper:
        return False
    else:
        mid_index = (lower + upper) // 2
        if item == L[mid_index]:
            return True
        elif item < L[mid_index]:
            return binary_search_improved(L, item, lower, mid_index - 1)
        else:
            return binary_search_improved(L, item, mid_index + 1, upper)


def binary_search_iterative(L, item):
    lower, upper = 0, len(L)
    while upper - lower > 0:
        mid_index = (upper + lower) // 2
        if item == L[mid_index]:
            return True
        elif item < L[mid_index]:
            upper = mid_index
        else: 
            lower = mid_index
    return False

# SORTING AND BUBBLE SORT 

# Time Complexity - O(n^2)
def is_sorted(L):
    for i in range(len(L) - 1):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                return False
    return True


# Time Complexity - O(n)
def is_sorted_better(L):
    for i in range(len(L) - 1):
        if L[i] < L[i+1]:
            return False
    return True


# Sorting Approach One
# def bad_sort(L):
#     for i in range(len(L) - 1):
#         if L[i] < L[i+1]:
#             L[i], L[i+1] = L[i+1], L[i]
# if two items are out of order, switch them


# Time Complexity - O(n^2)
# Also called Bubble Sort Algorithm
def bad_sort(L):
    for el in range(len(L) - 1):
        for i in range(len(L) - 1 - el): # el stops the redundant loop in the last comparison
            if L[i] < L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]



# SELECTION SORT

# Sorting for smallest element
def selection_sort_min(L):
    min = i # assuming index 1 has the smallest value at start
    for i in range(len(L) - 1): # loop through array length - 1
        for j in range(i+1, len(L)):
            if L[j] < L[min]: # looping through unsorted values
                min = j # finds new unsorted min postion 
        L[i], L[min] = L[min], L[i] # swap positions

def selection_sort_max(L):
    for i in range(len(L) - 1):
        max = 0
        for j in range(1, len(L)-i): # move backwards in array
            if L[j] > L[max]:
                max = j # finds new max from unsorted values
        L[-1 - i], L[max] = L[max], L[-1 - i] # swaps position
        