# -*- coding: utf-8 -*-


def merge(left, right):
    #array to store the sorted list
    sorted_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        merge_sort.count += 1
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def _merge_sort(li):
    "function to compute merge-sort"
    if len(li) == 1:
        return li

    middle = len(li) / 2
    left_li = _merge_sort(li[:middle])
    right_li = _merge_sort(li[middle:])
    sorted_list = merge(left_li, right_li)
    return sorted_list


def merge_sort(A, first, last):
    merge_sort.count = 0
    SA = _merge_sort(A[first:last])
    A = A[:first] + SA + A[last:]
    return A, merge_sort.count


if __name__ == "__main__":
    A = [10, 5, 2, 3, 7, 4, 8, 9, 11, 3, 1, 555,
         112, 31, 5, 12, 31, 51, 51, 1224, 151, 23, 12, 51, 67, 132451, 24]
    print(A)
    SA, compare_cnt = merge_sort(A, 0, 11)
    print(A)
    print("Compare Count : {}".format(compare_cnt))
    print(SA[:5])
    print(SA[5:11])
    print(SA[11:])
