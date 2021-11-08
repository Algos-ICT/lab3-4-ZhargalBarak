import random
import time


def part3(A, f, l):
    cur = A[f]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l+1):
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

M = []
n = 100
for i in range(n):
    M.append(random.randint(-10**6, 10**6))
start = time.perf_counter()
randomized_quick_sort(M, 0, n-1)
print(time.perf_counter() - start)
f = open('output.txt', 'w')
for i in range(n):
    f.write(str(M[i]) + ' ')
f.close()