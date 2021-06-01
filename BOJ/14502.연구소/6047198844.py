#세로크기, 가로크기
import collections
import copy
from itertools import combinations

def spread_virus(board):
    safe_cnt = 0
    Q = collections.deque()
    for y in range(N):
        for x in range(M):
            if board[y][x] == 2:
                Q.append((y,x))
            elif board[y][x] == 0:
                safe_cnt += 1
    while Q:
        #바이러스 위치
        vy, vx = Q.popleft()
        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            ny = vy + dy
            nx = vx + dx
            if (0 <= ny < N and 0 <= nx < M) and board[ny][nx] == 0:
                board[ny][nx] = 2
                safe_cnt -= 1
                Q.append((ny, nx))
    return safe_cnt

N, M = map(int, input().split())
#실수
board = [list(map(int, input().split())) for y in range(N)]
zero_pos = [(y, x) for y in range(N) for x in range(M) if board[y][x] == 0]
res = -1

for wall1, wall2, wall3 in combinations(zero_pos, 3):
    y_wall1, x_wall1 = wall1
    y_wall2, x_wall2 = wall2
    y_wall3, x_wall3 = wall3

    board[y_wall1][x_wall1] = 1
    board[y_wall2][x_wall2] = 1
    board[y_wall3][x_wall3] = 1
    res = max(res, spread_virus(copy.deepcopy(board)))
    board[y_wall1][x_wall1] = 0
    board[y_wall2][x_wall2] = 0
    board[y_wall3][x_wall3] = 0

print(res)