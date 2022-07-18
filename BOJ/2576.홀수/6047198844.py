import sys

arr = []
for _ in range(7):
    i = int(input())
    if i % 2 == 1:
        arr.append(i)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)