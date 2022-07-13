import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(board):
    check_board = [[True for _ in range(M)] for _ in range(N)]

    check_board[0][0] = False
    visited = set()
    visited.add((0, 0))
    Q = deque([(0, 0)])

    while Q:
        y, x = Q.popleft()
        for ny, nx in (y + 1, x), (y, x + 1), (y, x - 1), (y - 1, x):
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in visited and board[ny][nx] == 0:
                check_board[ny][nx] = False
                Q.append((ny, nx))
                visited.add((ny, nx))

    res = False
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                continue
            res = True
            cnt = 0
            for ny, nx in (y + 1, x), (y, x + 1), (y, x - 1), (y - 1, x):
                if 0 <= ny < N and 0 <= nx <= M and check_board[ny][nx] == False:
                    cnt += 1
            if cnt >= 2:
                board[y][x] = 0
    return res

res = 0
while bfs(board):
    res += 1
print(res)