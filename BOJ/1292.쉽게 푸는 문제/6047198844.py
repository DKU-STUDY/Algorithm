import sys

arr = [0]
for i in range(1, 50 + 1):
    for _ in range(i):
        arr.append(i)
s = [0]
for i in range(1, len(arr)):
    s.append(s[i-1] + arr[i])

A, B = map(int, sys.stdin.readline().split())
print(s[B] - s[A-1])