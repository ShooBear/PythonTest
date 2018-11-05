import random, time

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    quick_sort.move_cnt += 3


def partition(A, first, last):
    pivotindex = random.randint(first, last)
    pivotValue = A[pivotindex]

    swap(A, pivotindex, last)

    storeIndex = first

    for i in range(first, last):
        quick_sort.compare_cnt += 1
        if A[i] < pivotValue:
            swap(A, i, storeIndex)
            storeIndex += 1
    swap(A, storeIndex, last)
    return storeIndex


def _quick_sort(A, first, last):
    if first < last:
        p = partition(A, first, last)
        _quick_sort(A, first, p - 1)
        _quick_sort(A, p + 1, last)

def quick_sort(A, first, last):
    quick_sort.compare_cnt = 0
    quick_sort.move_cnt = 0
    _quick_sort(A, first, last)
    return quick_sort.compare_cnt, quick_sort.move_cnt


def merge(left, right):
    sorted_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        merge_sort.compare_cnt += 1
        if left[i] < right[j]:
            merge_sort.move_cnt += 1
            sorted_list.append(left[i])
            i += 1
        else:
            merge_sort.move_cnt += 1
            sorted_list.append(right[j])
            j += 1

    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def _merge_sort(A):
    if len(A) == 1:
        return A

    middle = int(len(A) / 2)
    left_A = _merge_sort(A[:middle])
    right_A = _merge_sort(A[middle:])
    sorted_list = merge(left_A, right_A)
    return sorted_list


def merge_sort(A, first, last):
    merge_sort.compare_cnt = 0
    merge_sort.move_cnt = 0

    SA = _merge_sort(A)
    A[first:last] = SA[0:len(SA) - 1]
    return merge_sort.compare_cnt, merge_sort.move_cnt


def check_sorted(A):
    sorted = True
    for i in range(n-1):
        if A[i] > A[i+1]: return False
    return True

print("Input n :")
n = int(input())
random.seed()
A, B = [], []

for i in range(n):
    r = random.randint(-1000, 1000)
    A.append(r)
    B.append(r)

# A, B에 n개의 같은 랜덤 값을 만들어 저장한다


t0 = time.clock()
cmp_quick, move_quick = quick_sort(A, 0, n-1)
t1 = time.clock()
cmp_merge, move_merge = merge_sort(B, 0, n-1)
t2 = time.clock()

# 진짜 정렬되었는지 check한다 - check_sorted를 호출
assert(check_sorted(A))
assert(check_sorted(B))

print("Quick sort: n =", n)
print("time = {} seconds".format(t1-t0))
print("comparisons = {}, moves = {}".format(cmp_quick, move_quick))
print("Merge sort: n =", n)
print("time = {} seconds".format(t2-t1))
print("comparisons = {}, moves = {}".format(cmp_merge, move_merge))