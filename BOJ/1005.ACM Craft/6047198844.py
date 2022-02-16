import heapq
import math
import sys
from collections import defaultdict, deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(lambda i: -int(i), sys.stdin.readline().split()))

    # edge 를 반대로.
    edges = defaultdict(list)
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        edges[Y].append(X)

    # 거리를 음수로.
    dist = [math.inf for _ in range(N + 1)]
    Q = deque([])
    W = int(sys.stdin.readline())

    # 시작점이 시작점으로 부터 가장 최소거리이다.
    Q.append((D[W], W))
    # heapq.heappush(Q, (D[W], W))
    dist[W] = D[W]

    while Q:
        # V 까지 오는데 최소 비용.
        # C, V = heapq.heappop(Q)
        C, V = Q.popleft()

        # 이미 최소비용이 갱신됨.
        if dist[V] < C:
            continue

        # 최소비용을 가지고 갱신을 해보자.
        for U in edges[V]:
            # C 는 V까지오는데 최소비용. D[U] 는 U까지 가는 간선의 가중치.
            # 따라서 그 합은 출발점에서 U 까지 가는 비용이다.
            if dist[U] > C + D[U]:
                dist[U] = dist[V] + D[U]
                Q.append((dist[U], U))
    print(-min(dist))
