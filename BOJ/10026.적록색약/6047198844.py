import re
import collections


def bfs(i, j, board):
    color = board[i][j]
    board[i][j] = 'Z'
    Q = collections.deque()
    Q.append((i, j))
    while Q:
        y, x = Q.popleft()
        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == color:
                board[ny][nx] = 'Z'
                Q.append((ny, nx))


N = int(input())
able_board = [list(input()) for _ in range(N)]
disabled_board = [list(re.sub('G', 'R', ''.join(row))) for row in able_board]

able_res = 0
for y in range(N):
    for x in range(N):
        if able_board[y][x] != 'Z':
            bfs(y, x, able_board)
            able_res += 1

disabled_res = 0
for y in range(N):
    for x in range(N):
        if disabled_board[y][x] != 'Z':
            bfs(y, x, disabled_board)
            disabled_res += 1

print(able_res, disabled_res)
