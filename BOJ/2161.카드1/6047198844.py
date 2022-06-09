from collections import deque

N = int(input())
arr = deque(list(range(1, N+1)))
while arr:
    print(arr.popleft(), end=' ')
    if arr:
        t = arr.popleft()
        arr.append(t)
