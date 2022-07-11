import sys

L, P = map(int, sys.stdin.readline().split())
C = L * P
for i in map(int, sys.stdin.readline().split()):
    print(i-C, end=' ')