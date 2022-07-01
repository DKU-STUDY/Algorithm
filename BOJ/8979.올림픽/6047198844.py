import sys

N, K = map(int, sys.stdin.readline().split())
arr = list()
table = dict()

for _ in range(N):
    i, *j = map(int, sys.stdin.readline().split())
    table[i] = j
    arr.append(j)
arr.sort()
print(arr.index(table[K]) + 1)