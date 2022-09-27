import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
res = abs(A-B)
for _ in range(N):
    i = int(sys.stdin.readline())
    res = min(abs(B-i)+1, res)
print(res)