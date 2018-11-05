import random


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def quicksort(A, law, high):
    if law < high:
        p = partition(A, law, high)
        quicksort(A, law, p - 1)
        quicksort(A, p + 1, high)


def partition(A, law, high):
    pivotindex = random.randint(law, high)
    pivotValue = A[pivotindex]

    swap(A, pivotindex, high)

    storeIndex = law

    for i in range(law, high):
        if A[i] < pivotValue:
            swap(A, i, storeIndex)
            storeIndex += 1
    swap(A, storeIndex, high)
    return storeIndex


l = list()
for i in range(99999):
    l.append(random.randint(-1000, 1000))

quicksort(l, 0, len(l) - 1)
print(l)
