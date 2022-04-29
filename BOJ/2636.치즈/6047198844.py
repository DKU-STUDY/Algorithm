import sys
from collections import deque

# 세로/가로
M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


# 겉
def func():
    Q = deque()
    Q.append((0, 0))
    board[0][0] = 3

    while Q:
        y, x = Q.popleft()
        for ny, nx in (y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1):
            if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 0:
                Q.append((ny, nx))
                board[ny][nx] = 3


# 녹는곳 -> 상하좌우 한면이라도 노출되어있는곳
def melt():
    Q = deque()
    for y in range(M):
        for x in range(N):
            for ny, nx in (y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1):
                if board[y][x] == 1 and 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 3:
                    Q.append((y, x))
                    board[y][x] = 5
                    break
    for y in range(M):
        for x in range(N):
            if board[y][x] == 3 or board[y][x] == 5:
                board[y][x] = 0

    return len(Q)

res = 0
cnt = 0
while True:
    func()
    tmp = melt()
    if tmp == 0:
        print(cnt)
        print(res)
        break

    cnt += 1
    res = tmp