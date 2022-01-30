import sys

R, C, Q = map(int, input().split())
board = [[0] * (C + 1)] + [[0] + list(map(int, input().split())) for _ in range(R)]
memo = [[0 for i in range(C + 1)] for j in range(R + 1)]

for y in range(1, R + 1):
    for x in range(1, C + 1):
        memo[y][x] = memo[y - 1][x] + memo[y][x - 1] - memo[y - 1][x - 1] + board[y][x]

for input in sys.stdin:
    r1, c1, r2, c2 = map(int, input.split())
    print((memo[r2][c2] + memo[r1 - 1][c1 - 1] - memo[r1 - 1][c2] - memo[r2][c1 - 1]) // ((r2 - r1 + 1) * (c2 - c1 + 1))) # 중복되어서 빼지는 사각형은 더한다.
