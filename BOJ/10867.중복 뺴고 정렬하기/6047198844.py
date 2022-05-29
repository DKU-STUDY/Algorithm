import sys

N = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))
for i in sorted(arr):
    print(i, end=' ')