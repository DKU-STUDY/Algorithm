def dp(triangle, y, x, n):
    if y == n:
        return 0

    if memo[y][x] != -1:
        return memo[y][x]

    memo[y][x] = triangle[y][x] + max(dp(triangle, y + 1, x, n), dp(triangle, y + 1, x + 1, n))

    return memo[y][x]


def solution(triangle):
    answer = 0
    global memo
    memo = [[-1 for _ in range(i)] for i in range(1, len(triangle) + 1)]

    return dp(triangle, 0, 0, len(triangle))