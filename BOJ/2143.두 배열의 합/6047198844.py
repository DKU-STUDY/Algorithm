import math
import sys
from collections import Counter


def arr_sum(acc, arr, limit):
    for i in range(limit):
        for j in range(i, limit):
            if i == j:
                acc[i][j] = arr[i]
            else:
                acc[i][j] = acc[i][j - 1] + arr[j]


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_acc = [[math.inf for _ in range(n)] for _ in range(n)]
B_acc = [[math.inf for _ in range(m)] for _ in range(m)]

arr_sum(A_acc, A, n)
arr_sum(B_acc, B, m)

a_counter = Counter()
b_counter = Counter()

for r in A_acc:
    a_counter += Counter(r)
for r in B_acc:
    b_counter += Counter(r)

res = 0
for i in a_counter:
    if b_counter.get(T - i):
        res += a_counter.get(i) * b_counter.get(T - i)
print(res)
