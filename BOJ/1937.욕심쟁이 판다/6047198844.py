import sys
sys.setrecursionlimit(10**9)

def dp(y, x):
    if memo[y][x] != -1:
        return memo[y][x]

    cnt = 0
    for ny, nx in (y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1):
        if 0 <= ny < N and 0 <= nx < N and board[y][x] < board[ny][nx]:
            cnt = max(cnt, dp(ny, nx))
    memo[y][x] = cnt + 1
    return memo[y][x]


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1] * N for _ in range(N)]

res = -1

for y in range(N):
    for x in range(N):
        res = max(res, dp(y, x))
print(res)
