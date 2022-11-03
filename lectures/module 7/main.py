# INSERTION SORT

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i] # our current value
        j = i-1 # our previous value
        while j >= 0 and key < L[j]: # while j is not 0, and current value less than prev
            L[j+1] = L[j] #move our values up until current value is greater than prev
        L[j+1] = key #value swapped

# MERGE SORT

def merge_sort(D):
    n = len(D)
    if n > 1:
        mid = n // 2
        D1 = D[:mid]
        D2 = D[mid:]

        merge_sort(D1)
        merge_sort(D2)

        merge(D1, D2, D)


def merge(D1, D2, D):
    i = j = 0
    while i < len(D1) and j < len(D1):
        if D1[i] < D2[j]:
            D[i+j] = D1[i]
        else:
            D[i+j] = D2[j]
            j += 1
    D[i+j:] = D1[i:] + D2[:i]

# QUICK SORT 

# def quick_sort(D, L_indx, H_idx):
#     if L_indx < H_idx:
#         pivot = partition(D, L_indx, H_idx)
#         quick_sort(D, L_indx, pivot - 1)
#         quick_sort(D, pivot + 1, H_idx)

# def partition(D, low, high):
#     pivotIndex = (low + high) // 2
#     swap(pivotIndex, high)
#     i = low
#     for j in range(low, high+1):
#         if D[j] <= D[high]:
#             swap(i, j)
#             i += 1
#     return i-1