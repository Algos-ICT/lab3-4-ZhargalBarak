import random

def part3(A, f, l):
    cur = A[f][0]
    left = [[], []]
    mid = [[], []]
    right = [[], []]
    j = 0
    count = 0
    for i in range(f, l + 1):
        if A[i][0] < cur:
            left[0].append(A[i][0])
            left[1].append(A[i][1])
            j += 1
        elif A[i][0] == cur:
            mid[0].append(A[i][0])
            mid[1].append(A[i][1])
            count += 1
        else:
            right[0].append(A[i][0])
            right[1].append(A[i][1])
    total0 = left[0] + mid[0] + right[0]
    total1 = left[1] + mid[1] + right[1]
    for i in range(len(total0)):
        A[f+i][0] = total0[i]
        A[f+i][1] = total1[i]
    return f + j, f + j + count - 1

def part3_under(A, f, l):
    cur = A[f][1]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(f, l + 1):
        if A[i][1] < cur:
            left.append(A[i][1])
            j += 1
        elif A[i][1] == cur:
            mid.append(A[i][1])
            count += 1
        else:
            right.append(A[i][1])
    total = left + mid + right
    for i in range(len(total)):
        A[f+i][1] = total[i]
    return f + j, f + j + count - 1


def randomized_quick_sort_under(A, f ,l):
    if f < l:
        k = random.randint(f, l)
        A[f][1], A[k][1] = A[k][1], A[f][1]
        m1, m2 = part3_under(A, f, l)
        randomized_quick_sort_under(A, f, m1-1)
        randomized_quick_sort_under(A, m2+1, l)

def randomized_quick_sort(A, f, l):
    if f < l:
        k = random.randint(f, l)
        A[f], A[k] = A[k], A[f]
        m1, m2 = part3(A, f, l)
        randomized_quick_sort(A, f, m1-1)
        randomized_quick_sort_under(A, m1, m2)
        randomized_quick_sort(A, m2+1, l)

f = open('input.txt')
s, p = map(int, f.readline().split())
otrez = [list(map(int, f.readline().split())) for i in range(s)]
dots = list(map(int, f.readline().split()))
f.close()
randomized_quick_sort(otrez, 0, s-1)
f = open('output.txt', 'w')
for i in range(p):
    count = 0
    ind = 0
    while ind < s and dots[i] >= otrez[ind][0]:
        if dots[i] <= otrez[ind][1]:
            count += 1
        ind += 1
    f.write(str(count) + ' ')
print(otrez)
f.close()