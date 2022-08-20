import sys

N = int(input())
A, B = map(int, sys.stdin.readline().split())
print(min(A//2 + B, N))