import sys

N, L = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
for num in nums:
    if L >= num:
        L += 1
    else:
        break
print(L)