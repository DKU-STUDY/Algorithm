import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

arr = []
arr.append(A / C + B / D)
arr.append(C / D + A / B)
arr.append(D / B + C / A)
arr.append(B / A + D / C)
print(arr.index(max(arr)))