import sys

N = int(sys.stdin.readline())
res = 0
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    res += B % A
print(res)