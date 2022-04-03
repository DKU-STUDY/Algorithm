# O(NM) => 40,000 * 10,000 = 4억
# O(MlogN) => 10,000 * 200 = 2백만
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)

LOG = 21
N = int(sys.stdin.readline())
edges = defaultdict(list)

for _ in range(N - 1):
    v, w, distance = map(int, sys.stdin.readline().split())
    edges[v].append((w, distance))
    edges[w].append((v, distance))

visited = [0 for _ in range(N + 1)]
D = [0 for _ in range(N + 1)]
P = [[0 for _ in range(LOG + 1)] for _ in range(N + 1)]
C = [0 for _ in range(N + 1)]


def make_tree(V, depth, cost):
    visited[V] = 1
    C[V] = cost
    D[V] = depth

    for W, distance in edges[V]:
        if visited[W] != 1:
            P[W][0] = V
            make_tree(W, depth + 1, cost + distance)


# 루트를 1로 잡는다.
make_tree(1, 0, 0)

# 공통부모 세팅
for i in range(1, LOG):
    for j in range(1, N + 1):
        P[j][i] = P[P[j][i - 1]][i - 1]


def LCA(A, B):
    # 두노드의 높이를 맞춘다. 단 B는 항상 A 보다 높이가 낮다.
    if D[A] > D[B]:
        A, B = B, A

    # 역순으로 하지 않으면, 차이를 꽉 매우지 못할수도 있음.
    for i in range(LOG, -1, -1):
        if D[B] - D[A] >= 1 << i:
            B = P[B][i]

    # 두노드의 높이를 맞췄다면, 위에서 부터 공통 부모를 찾는다.
    # 이미 같으면 A를 반환한다.
    if A == B:
        return A

    for i in range(LOG, -1, -1):
        if P[A][i] != P[B][i]:
            A = P[A][i]
            B = P[B][i]

    return P[A][0]


M = int(sys.stdin.readline())
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    print(C[v] + C[w] - 2 * C[LCA(v, w)])
