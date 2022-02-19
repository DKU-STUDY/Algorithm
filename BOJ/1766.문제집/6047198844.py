import heapq
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
indegree = [0 for _ in range(N + 1)]
for _ in range(M):
    V, W = map(int, sys.stdin.readline().split())
    edges[V].append(W)
    indegree[W] += 1

# indegree 가 0 인 정점번호의 집합
Q = []
for idx in range(1, N + 1):
    if indegree[idx] == 0:
        heapq.heappush(Q, idx)

res = []
while Q:
    V = heapq.heappop(Q)
    res.append(V)
    for W in edges[V]:
        indegree[W] -= 1
        if indegree[W] == 0:
            heapq.heappush(Q, W)

print(' '.join(map(str, res)))