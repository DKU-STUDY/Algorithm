# (n-1)! / (n-m)! * m!
import sys

N, K = map(int, sys.stdin.readline().split())

arr = [1]
for i in range(1, 31):
    arr.append(arr[-1] * i)
print(arr[N - 1] // arr[(N - 1) - (K - 1)] // arr[K - 1])
