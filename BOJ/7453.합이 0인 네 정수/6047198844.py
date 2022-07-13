import sys
from collections import defaultdict
from itertools import product

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A, B, C, D = zip(*arr)
table = dict()
for i in A:
    for j in B:
        if i + j in table:
            table[i + j] += 1
        else:
            table[i + j] = 1
res = 0
for i in C:
    for j in D:
        if -(i + j) in table:
            res += table[-(i + j)]

print(res)
