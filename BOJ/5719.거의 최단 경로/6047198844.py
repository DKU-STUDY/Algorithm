import heapq
import math
import sys
from collections import defaultdict, deque


def dijkstra():
    PQ = []
    dist[S] = 0
    heapq.heappush(PQ, (dist[S], S))
    while PQ:
        P, V = heapq.heappop(PQ)

        # dist 는 최단거리임. P가 최단거리가 아니면 아래 과정을 수행하지 않음.
        if dist[V] != P:
            continue

        for W in edges[V]:
            # S -> V(최단거리 보장) + V -> W (연결거리) 갱신?
            if dist[W] > dist[V] + edges[V][W]:
                dist[W] = dist[V] + edges[V][W]
                heapq.heappush(PQ, (dist[W], W))


def track():
    remove = []

    Q = deque()
    Q.append(D)
    while Q:
        V = Q.popleft()
        if V == S:
            continue
        for pre_V, pre_P in r_edges[V]:
            if dist[pre_V] + edges[pre_V][V] == dist[V]:
                if (pre_V, V) not in remove:
                    Q.append(pre_V)
                    remove.append((pre_V, V))

    return remove


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    # S -> D
    S, D = map(int, sys.stdin.readline().split())
    edges = [dict() for _ in range(N)]
    r_edges = [list() for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        # U -> V : 비용 P
        edges[U][V] = P
        r_edges[V].append((U, P))

    dist = [math.inf for _ in range(N)]

    dijkstra()
    remove = track()

    for U, V in remove:
        del edges[U][V]

    dist = [math.inf for _ in range(N)]
    dijkstra()

    if dist[D] == math.inf:
        print(-1)
    else:
        print(dist[D])
