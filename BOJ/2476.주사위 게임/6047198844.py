import sys


def func(i, j, k):
    if i == j == k:
        return 10000 + i * 1000
    elif i == j or j == k:
        return 1000 + j * 100
    elif i == k:
        return 1000 + i * 100
    return max(i, j, k) * 100


N = int(sys.stdin.readline())
res = -1
for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    res = max(res, func(A[0], A[1], A[2]))

print(res)
