# 문제
# n(1≤n≤1,000)개의 도시가 있다.
# 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. -> 다익스트라 알고리즘
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.
#
# 입력
# 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
#
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
#
# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
#
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.
#
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.
#
# 풀이
# 한 정점에서 다른 정점까지가는데 드는 최소비용을 구할때도 다익스트라 알고리즘을 이용한다.
import heapq
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = defaultdict(list)
INF = 987654321

# 간선 입력
for _ in range(m):
    i, j, cost = map(int, input().split())
    edges[i].append((cost, j))

depart, arrive = map(int, input().split())

# 초기화. 출발 정점을 제외한 곳은 알수가 없다 -> 무한
distances = [INF for _ in range(n + 1)]
distances[depart] = 0
routes = [-1 for _ in range(n + 1)]

PQ = []
# cost , 정점
heapq.heappush(PQ, (0, depart))
# heap 이 종료될때까지
while PQ:
    cost, v = heapq.heappop(PQ)
    # 갱신되었는지? 현재값이 최적인지?
    if distances[v] != cost:
        continue
    # 최적값으로 갱신이 가능한지 확인한다.
    # 갱신 가능하다면. 경로와 갱신값을 PQ에 넣는다.
    for c, w in edges[v]:
        if distances[w] > cost + c:
            distances[w] = cost + c
            routes[w] = v
            heapq.heappush(PQ, (distances[w], w))

print(distances[arrive])

res = []
root = arrive
while root != -1:
    res.append(root)
    root = routes[root]
print(len(res))
for i in res[::-1]:
    print(i, end=' ')