import sys

N, M = map(int, sys.stdin.readline().split())
print(min(N//2, M//2))