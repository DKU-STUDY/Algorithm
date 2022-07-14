import sys

K, N, M = map(int, sys.stdin.readline().split())
print(max(0, K * N - M))