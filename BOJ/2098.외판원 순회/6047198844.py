import math
import sys
from collections import defaultdict

'''
2 ≤ N ≤ 16
DP + 비트마스킹
사이클이므로 어디서 시작하든 결과는 같다. 0번째 부터 시작한다.

TCP(visited, current) = 
visited 가 전부 가득 찼을 경우 -> 기저사례
     current -> 원점이 불가한 경우 무한대
     아닌 경우 간선 크기 반환

가득 차지 않은 경우 ->
min(TCP(visited U {k}, k) + edge[current][k]), k 는 visited의 여집합)

visited 는 비트마스킹으로 처리한다. 집합을 표현하기 편함.
'''

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1 for _ in range(1 << N)] for _ in range(N)]


def TSP(current, visited):
    # 모두 방문 한 경우
    if visited == (1 << N) - 1:
        if board[current][0] == 0:
            return math.inf
        else:
            return board[current][0]

    # 메모가 있는 경우
    if memo[current][visited] != -1:
        return memo[current][visited]

    res = math.inf
    # 모두 방문되지 않은 경우. 여집합을 방문한다.
    for k in range(N):
        if (visited & (1 << k)) != 0:
            continue
        if board[current][k] == 0:
            continue

        res = min(res, TSP(k, visited | (1 << k)) + board[current][k])

    memo[current][visited] = res
    return memo[current][visited]


print(TSP(0, 0 | (1 << 0)))
