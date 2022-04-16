# 정점 8개
# 0번 정점이 정보과학관
# 1번 정점이 전산관
# 2번 정점이 미래관
# 3번 정점이 신앙관
# 4번 정점이 한경직기념관
# 5번 정점이 진리관
# 6번 정점이 학생회관
# 7번 정점이 형남공학관
# D분 일때 해당 경로를 지난 경우.
# arr[D][경로]
import sys
from collections import defaultdict

memo = defaultdict(lambda: [[-1 for _ in range(1 + 7)] for _ in range(1 + 7)])

memo[1] = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]]


# 10억? log N 의 방법이 필요하다.

# frm -> to
# 거리가 D 만큼남았을때 A에서 C 까지 가는 경우의 수
def func(A, C, D):
    # 범위는 항상 안전하다.
    if memo[D][A][C] != -1:
        return memo[D][A][C]

    memo[D][A][C] = 0
    for B in range(7 + 1):
        # 곱!
        memo[D][A][C] += (func(A, B, D // 2) % 1000000007
                          * func(B, C, D // 2 + D % 2) % 1000000007) % 1000000007

    return memo[D][A][C] % 1000000007


D = int(sys.stdin.readline())
print(func(0, 0, D))
