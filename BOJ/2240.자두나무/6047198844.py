import math
import sys

T, W = map(int, sys.stdin.readline().split())
arr = [0] + [int(sys.stdin.readline()) for _ in range(T)]

memo = [[[0 for _ in range(T + 1)] for _ in range(W + 2)] for _ in range(2 + 1)]
# memo[나무][이동횟수][시간]

# 시간
for i in range(1, T + 1):
    # 이동횟수
    for j in range(1, W + 2):
        # 현재 값이 1인 경우
        if arr[i] == 1:
            # 1에 대해.
            # 이전이 1 인경우 / 이전이 2 인경우
            memo[1][j][i] = max(memo[1][j][i - 1], memo[2][j - 1][i - 1]) + 1
            # 2에 대해.
            # 이전이 0 인경우 / 이전이 1 인경우
            memo[2][j][i] = max(memo[1][j - 1][i - 1], memo[2][j][i - 1])
        # 현재 값이 2인 경우
        else:
            # 이동횟수 1번 / 떨어지는 초가 1인 경우
            if i == 1 and j == 1:
                continue

            # 1에 대해.
            # 이전이 1 인경우 / 이전이 2 인경우
            memo[1][j][i] = max(memo[1][j][i - 1], memo[2][j - 1][i - 1])
            # 2에 대해.
            # 이전이 0 인경우 / 이전이 1 인경우
            memo[2][j][i] = max(memo[1][j - 1][i - 1], memo[2][j][i - 1]) + 1

ans = -math.inf
for i in range(1, W + 2):
   ans = max(memo[1][i][T], memo[2][i][T])
print(ans)