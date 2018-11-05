import random

def merge(A, start, end):
	start = int(start)
	end = int(end)
	L = A[start:(start + end)/2+1]
	R = A[(start + end)/2 + 1:(end+1)]
	L.append(10**9)
	R.append(10**9)
	i = 0
	j = 0
	for k in range(start, end + 1):
		if L[i] > R[j]:
			A[k] = R[j]
			j = j + 1
		elif L[i] < R[j]:
			A[k] = L[i]
			i = i + 1

def mergesort(A, start, end):
	start = int(start)
	end = int(end)
	if len(A[start:(end+1)]) == 1:
		return A[start:(end+1)]
	elif len(A[start:(end+1)]) == 2:
		if A[start] > A[end]:
			A[start], A[end] = A[end], A[start]
		return A[start:(end+1)]
	else:
		mergesort(A, int(start), int(start+end)/2)
		mergesort(A, int((start+end)/2) + 1, int(end))
		merge(A, int(start), int(end))


def check_sorted(A):
    sorted = True
    for i in range(len(A)-1):
        if A[i] >= A[i+1]: return False
    return True


if __name__ == "__main__":
    A = list()
    for i in range(9):
        A.append(random.randint(-1000, 1000))
    print(A)
    SA, compare_cnt = mergesort(A, 0, len(A) - 1)
    print(SA)
    assert(check_sorted(SA))
    print("Compare Count : {}".format(compare_cnt))
