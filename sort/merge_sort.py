import random

def merge(left, right):
    #array to store the sorted list
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

    SA = _merge_sort(A[first:last])
    A[first:last] = SA[0:]
    A = A[:first] + SA + A[last:]
    return merge_sort.compare_cnt, merge_sort.move_cnt


def check_sorted(A):
    sorted = True
    for i in range(len(A)-1):
        if A[i] >= A[i+1]:
            return False
    return True


if __name__ == "__main__":

    A = list()
    for i in range(20):
        A.append(random.randint(-1000, 1000))
    print(A)
    compare_cnt, move_cnt = merge_sort(A, 0, len(A) - 1)
    print(A)
    assert(check_sorted(A))
    print("Compare Count : {} move_cnt : {}".format(compare_cnt, move_cnt))
