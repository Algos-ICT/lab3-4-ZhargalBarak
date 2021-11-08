import random
import time
import sys

def part(A, f, l):
    cur = A[1][f]
    j = f
    for i in range(f+1, l+1):
        if A[1][i] < cur:
            j += 1
            A[0][j], A[0][i] = A[0][i], A[0][j]
            A[1][j], A[1][i] = A[1][i], A[1][j]
    A[0][f], A[0][j] = A[0][j], A[0][f]
    A[1][f], A[1][j] = A[1][j], A[1][f]
    return j
    # left = [[], []]
    # mid = [[], []]
    # right = [[], []]
    # j = 0
    # for i in range(f, l + 1):
    #     if A[1][i] < cur:
    #         left[0].append(A[0][i])
    #         left[1].append(A[1][i])
    #         j += 1
    #     elif A[1][i] == cur:
    #         mid[0].append(A[0][i])
    #         mid[1].append(A[1][i])
    #     else:
    #         right[0].append(A[0][i])
    #         right[1].append(A[1][i])
    # # totalA = left[0] + mid[0] + right[0]
    # # total0 = left[1] + mid[1] + right[1]
    # # total1 = left[2] + mid[2] + right[2]
    # # for i in range(len(totalA)):
    # #     A[f+i] = totalA[i]
    # #     B[0][f+i] = total0[i]
    # #     B[1][f+i] = total1[i]
    # A[0][f:l + 1] = left[0] + mid[0] + right[0]
    # A[1][f:l + 1] = left[1] + mid[1] + right[1]
    # # sort_B(B, f+j, f+j+count-1)
    # return f + j

def quick_sort(A, f, l):
    if f < l:
        maxI = -1
        minI = 10**8
        for i in range(f, l+1):
            if A[1][i] > maxI:
                maxI = A[1][i]
            if A[1][i] < minI:
                minI = A[1][i]
        medI = (maxI + minI) // 2
        dif = 10**8
        k = random.randint(f, l)
        for i in range(f, l+1):
            if abs(medI - i) < dif:
                k = i
                dif = abs(medI - i)
                if dif == 0:
                    break
        A[0][f], A[0][k] = A[0][k], A[0][f]
        A[1][f], A[1][k] = A[1][k], A[1][f]
        m = part(A, f, l)
        quick_sort(A, f, m - 1)
        quick_sort(A, m + 1, l)

def alph(A, l):
    letter = [[[], []] for _ in range(26)]
    global res
    for i in range(l):
        letter[ord(A[i])-97][0].append(res[0][i])
        letter[ord(A[i])-97][1].append(res[1][i])
    global ind, m
    if ind != m-1:
        for i in range(26):
            quick_sort(letter[i], 0, len(letter[i][0])-1)
    j = 0
    for i in range(26):
        lgth = len(letter[i][0])
        res[0][j:j + lgth] = letter[i][0][0:lgth]
        res[1][j:j + lgth] = letter[i][1][0:lgth]
        j += lgth

sys.setrecursionlimit(1000000)
with open('input.txt') as f:
    n, m, k = map(int, f.readline().split())
    cyber = [list(f.readline()) for _ in range(m)]
res = [list(range(1, n+1)) for _ in range(2)]
start = time.perf_counter()
for i in range(1, k+1):
    ind = m-i
    alph(cyber[ind], n)
    if ind != m-k:
        for i in range(n):
            res[1][res[0][i]-1] = i+1
        res[0] = list(range(1, n+1))
sec = time.perf_counter() - start
with open('output.txt', 'w') as f:
    for i in range(n):
        f.write(str(res[0][i]) + ' ')
print(sec)