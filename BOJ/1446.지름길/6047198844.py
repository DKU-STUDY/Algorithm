# 문제
# 차를 타고 D킬로미터 길이의 고속도로를 지난다.
# 고속도로에 지름길이 존재. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.
#
# 세준이가 운전해야 하는 거리의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다.
# 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.
#
# 출력
# 세준이가 운전해야하는 거리의 최솟값을 출력하시오.

# 한정점에서 다른 정점까지 가는데 최소거리 -> 다익스트라 활용가능.
import heapq
from collections import defaultdict

INF = 987654321
N, D = map(int, input().split())
edges = defaultdict(lambda: dict())
vertexes = set()
for _ in range(N):
    i, j, cost = map(int, input().split())
    # edges 필터링. 유일한 간선만 만들어보자.
    if j not in edges[i] or edges[i][j] > cost:
        edges[i][j] = cost
    vertexes.add(i)
    vertexes.add(j)

depart, arrive = 0, D
vertexes.add(0)
vertexes.add(D)

vertexes = list(vertexes)
for i in vertexes:
    for j in vertexes:
        if i < j and (j not in edges[i] or edges[i][j] > j - i):
            edges[i][j] = j - i

# 최단거리 초기화
distance = dict()
for v in vertexes:
    distance[v] = INF
distance[0] = 0

PQ = []
# cost, 정점
heapq.heappush(PQ, (0, 0))
while PQ:
    cm, mid = heapq.heappop(PQ)
    # 최적이 아니면 버린다.
    if distance[mid] != cm:
        continue
    # 최적인 경우이므로 해당 경우로 최적화 가능한지 묻고, 가능하면 우선순위 큐에 넣는다.
    # == cm까지의 최적 경로 + mid -> end 의 경로 < ce 까지의 최적경로
    for end, ce in edges[mid].items():
        if distance[mid] + ce < distance[end]:
            distance[end] = distance[mid] + ce
            heapq.heappush(PQ, (distance[end], end))

print(distance[D])