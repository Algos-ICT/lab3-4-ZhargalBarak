import random
import time


def part3(A, f, l):
    cur = A[f][0] ** 2 + A[f][1] ** 2
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l+1):
        r = A[i][0] ** 2 + A[i][1] ** 2
        if r < cur:
            left.append(A[i])
            j += 1
        elif r == cur:
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

n, K = map(int, input().split())
dots = [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for i in range(n)]
start = time.perf_counter()
randomized_quick_sort(dots, 0, n-1)
print(dots)
print(time.perf_counter() - start)
f = open('output.txt', 'w')
for i in range(K-1):
    f.write(str(dots[i]) + ',')
f.write(str(dots[K-1]))
f.close()