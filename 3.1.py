import copy
import random

def part3(A, f, l):
    cur = A[f]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l + 1):
        if A[i] < cur:
            left.append(A[i])
            j += 1
        elif A[i] == cur:
            mid.append(A[i])
            count += 1
        else:
            right.append(A[i])
    A[f:l+1] = left + mid + right
    return f+j, f+j+count-1

def randomized_quick_sort(A, f, l):
    if f < l:
        k = random.randint(f, l)
        A[f], A[k] = A[k], A[f]
        m1, m2 = part3(A, f, l)
        randomized_quick_sort(A, f, m1-1)
        randomized_quick_sort(A, m2+1, l)

f = open('input.txt')
n, k = map(int, f.readline().split())
M = list(map(int, f.readline().split()))
f.close()
Sorted = copy.copy(M)
for i in range(k):
        M1 = []
        ind = i
        len = 0
        while ind <= n-1:
            M1.append(Sorted[ind])
            ind += k
            len += 1
        randomized_quick_sort(M1, 0, len-1)
        for j in range(len):
            Sorted[i + j*k] = M1[j]
randomized_quick_sort(M, 0, n-1)
if Sorted == M:
    print('ДА')
else:
    print('НЕТ')