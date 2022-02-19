# 문제
# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 각 길마다 길을 유지하는데 드는 유지비가 있다.
# 마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다.
# 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
# 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.
#
# 그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다.
# 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
# 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다. 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.
#
# 출력
# 첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
Q = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(Q, (C, A, B))

P = [-1 for _ in range(N + 1)]


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return
    P[PB] = PA


def find(A):
    if P[A] == -1:
        return A
    P[A] = find(P[A])
    return P[A]


res = []
while Q:
    cost, A, B = heapq.heappop(Q)

    PA = find(A)
    PB = find(B)

    if PA == PB:
        continue

    res.append(cost)
    union(PA, PB)

print(sum(res[:-1]))
