import random


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    quicksort.move_cnt += 3


def partition(A, first, last):
    pivotindex = random.randint(first, last)
    pivotValue = A[pivotindex]

    swap(A, pivotindex, last)

    storeIndex = first

    for i in range(first, last):
        quicksort.compare_cnt += 1
        if A[i] < pivotValue:
            swap(A, i, storeIndex)
            storeIndex += 1
    swap(A, storeIndex, last)
    return storeIndex


def _quicksort(A, first, last):
    if first < last:
        p = partition(A, first, last)
        _quicksort(A, first, p - 1)
        _quicksort(A, p + 1, last)

def quicksort(A, first, last):
    quicksort.compare_cnt = 0
    quicksort.move_cnt = 0
    _quicksort(A, first, last)
    return quicksort.compare_cnt, quicksort.move_cnt


l = list()
for i in range(999):
    l.append(random.randint(-1000, 1000))

compare_cnt, move_cnt = quicksort(l, 0, len(l) - 1)
print(compare_cnt)
print(move_cnt)
