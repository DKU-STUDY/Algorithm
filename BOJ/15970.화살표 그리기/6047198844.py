import math
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort()

res = 0
for i in range(len(arr)):
    left = i - 1
    right = i + 1
    diff = math.inf
    while left >= 0:
        if arr[left][1] == arr[i][1]:
            diff = min(diff, arr[i][0] - arr[left][0])
            break
        else:
            left -= 1
    while right < len(arr):
        if arr[right][1] == arr[i][1]:
            diff = min(diff, arr[right][0] - arr[i][0])
            break
        else:
            right += 1
    res += diff
print(res)