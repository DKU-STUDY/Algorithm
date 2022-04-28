import heapq
import math
import sys
from collections import defaultdict

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    # S -> D
    S, D = map(int, sys.stdin.readline().split())
    edges = defaultdict(list)

    for _ in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        # U -> V : 비용 P
        edges[U].append((P, V))

    PQ = []
    dist = [math.inf for _ in range(N)]
    dist[S] = 0
    heapq.heappush(PQ, (dist[S], S))
    pre = [i for i in range(N)]
    visited = set()

    while PQ:
        P, V = heapq.heappop(PQ)

        # dist 는 최단거리임. P가 최단거리가 아니면 아래 과정을 수행하지 않음.
        if dist[V] != P and V in visited:
            continue

        for PP, W in edges[V]:
            # S -> V(최단거리 보장) + V -> W (연결거리) 갱신?
            if dist[W] > dist[V] + PP:
                dist[W] = dist[V] + PP
                pre[W] = V
                heapq.heappush(PQ, (dist[W], W))

    print(pre)

    H = D
    while H != 0:
        PH = pre[H]
        visited.add(PH)


