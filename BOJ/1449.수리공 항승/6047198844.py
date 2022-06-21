from collections import deque

N, L = map(int, input().split())
arr = deque(sorted(map(int, input().split())))

start = arr.popleft() - 0.5
cnt = 1
while arr:
    tmp = arr.popleft()
    if start + L >= tmp + 0.5:
        pass
    else:
        start = tmp - 0.5
        cnt += 1

print(cnt)