# 11명의 선수가 0 ~ 100
import sys

input = sys.stdin.readline


def solve(y, total, memo):
    if y == 11:
        return total

    answer = 0
    for x in range(11):
        if memo[x]:
            continue
        if players[y][x] == 0:
            continue
        total += players[y][x]
        memo[x] = True
        answer = max(answer, solve(y + 1, total, memo))
        total -= players[y][x]
        memo[x] = False

    return answer


C = int(input())
for _ in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]
    memo = [False for _ in range(11)]
    print(solve(0, 0, memo))
