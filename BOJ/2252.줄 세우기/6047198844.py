import sys
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
indegrees = [0 for _ in range(N+1)]

for _ in range(M):
    V, W = map(int, sys.stdin.readline().split())
    # V 에 연결된 간선들을 나타내게 된다.
    edges[V].append(W)
    indegrees[W] += 1

# indegree 가 없는 정점들의 집합.
Q = deque([])
for V in range(1, N + 1):
    if indegrees[V] == 0:
        Q.append(V)

res = []
while Q:
    V = Q.popleft()
    # 결과에 삽입한다.
    res.append(V)

    # 자신으로부터 나가는 간선을 제거한다. 간선 제거후 연결된 정점에 대해서 indegree 감소를 시키며, 이떄의 정점이 0이되면 Q에 추가한다.
    for W in edges[V]:
        indegrees[W] -= 1
        if indegrees[W] == 0:
            Q.append(W)

for i in res:
    print(i, end=' ')
