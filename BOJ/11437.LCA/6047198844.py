import sys
from collections import defaultdict, deque

LOG = 15
N = int(sys.stdin.readline())
edges = defaultdict(list)
for _ in range(N-1):
    V, W = map(int, sys.stdin.readline().split())
    edges[V].append(W)
    edges[W].append(V)

D = [0 for _ in range(N + 1)]
P = [[-1 for _ in range(LOG+1)]for _ in range(N + 1)]

visited = set()


def make_tree(V, depth):
    visited.add(V)
    D[V] = depth

    for W in edges[V]:
        if W not in visited:
            make_tree(W, depth + 1)
            P[W][0] = V


make_tree(1, 0)

for i in range(1, LOG+1):
    for j in range(N+1):
        P[j][i] = P[P[j][i-1]][i-1]


def LCA(A, B):
    if D[B] < D[A]:
        A, B = B, A

    for i in range(LOG, -1, -1):
        if D[B] - D[A] >= 1 << i:
            B = P[B][i]

    if A == B:
        return A

    for i in range(LOG, -1, -1):
        if P[A][i] != P[B][i]:
            A = P[A][i]
            B = P[B][i]

    return P[A][0]


M = int(sys.stdin.readline())
for _ in range(M):
    V, W = map(int, sys.stdin.readline().split())
    print(LCA(V,W))