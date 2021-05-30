#y,x좌표에서 중복없이 갈수있는 최대의 수.
from functools import lru_cache

R, C = map(int, input().split())
board = [list(input())for _ in range(R)]
path = set()


def dfs(y, x):
    res = 1
    path.add(board[y][x])
    for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in path:
            res = max(res, 1 + dfs(ny, nx))
    path.remove(board[y][x])
    return res

print(dfs(0, 0))