# 문제
# N개의 도시와 그 도시를 연결하는 N-1개의 도로로 이루어진 도로 네트워크가 있다.
#
# 모든 도시의 쌍에는 그 도시를 연결하는 유일한 경로가 있고, 각 도로의 길이는 입력으로 주어진다.
#
# 총 K개의 도시 쌍이 주어진다. 이때, 두 도시를 연결하는 경로 상에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (2 ≤ N ≤ 100,000)
#
# 다음 N-1개 줄에는 도로를 나타내는 세 정수 A, B, C가 주어진다. A와 B사이에 길이가 C인 도로가 있다는 뜻이다. 도로의 길이는 1,000,000보다 작거나 같은 양의 정수이다.
#
# 다음 줄에는 K가 주어진다. (1 ≤ K ≤ 100,000)
#
# 다음 K개 줄에는 서로 다른 두 자연수 D와 E가 주어진다. D와 E를 연결하는 경로에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 구해서 출력하면 된다.
#
# 출력
# 총 K개 줄에 D와 E를 연결하는 경로에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 출력한다.
import math
import sys
from collections import defaultdict, deque

LOG = 20
N = int(sys.stdin.readline())
PV = [[0] * LOG for _ in range(N + 1)]
PC = [[(math.inf, -math.inf)] * LOG for _ in range(N + 1)]
D = [0] * (N + 1)
edges = defaultdict(list)
for _ in range(N - 1):
    A, B, C = map(int, sys.stdin.readline().split())
    edges[A].append((B, C))
    edges[B].append((A, C))


def make_tree(root):
    visited = set()
    visited.add(root)

    Q = deque()
    Q.append(root)
    depth = 0
    while Q:
        depth += 1
        for _ in range(len(Q)):
            V = Q.popleft()
            for W, C in edges[V]:
                if W not in visited:
                    visited.add(W)
                    Q.append(W)
                    PV[W][0] = V
                    PC[W][0] = (C, C)
                    D[W] = depth


make_tree(1)

for i in range(1, LOG):
    for W in range(1, N + 1):
        PV[W][i] = PV[PV[W][i - 1]][i - 1]

        mina, maxa = PC[PV[W][i - 1]][i - 1]
        minb, maxb = PC[W][i - 1]

        PC[W][i] = min(mina, minb), max(maxa, maxb)


def LCA(A, B):
    # B가 항상 더 깊도록한다.
    if D[A] > D[B]:
        A, B = B, A

    MNA, MXA = math.inf, -math.inf
    MNB, MXB = math.inf, -math.inf

    # 본래 정점.
    for i in range(LOG - 1, -1, -1):
        if D[B] - D[A] >= 1 << i:
            MNB, MXB = min(PC[B][i][0], MNB), max(PC[B][i][1], MXB)
            B = PV[B][i]

    if A != B:
        # 높이가 같다. 최소 부모의 위치를 찾자.
        for i in range(LOG - 1, -1, -1):
            if PV[A][i] != PV[B][i]:
                MNA, MXA = min(PC[A][i][0], MNA), max(PC[A][i][1], MXA)
                MNB, MXB = min(PC[B][i][0], MNB), max(PC[B][i][1], MXB)
                A = PV[A][i]
                B = PV[B][i]

        MNA, MXA = min(PC[A][0][0], MNA), max(PC[A][0][1], MXA)
        MNB, MXB = min(PC[B][i][0], MNB), max(PC[B][i][1], MXB)
        print(min(MNA, MNB), max(MXA, MXB))
    else:
        print(MNB, MXB)


K = int(sys.stdin.readline())
for _ in range(K):
    q, w = map(int, sys.stdin.readline().split())
    LCA(q, w)
