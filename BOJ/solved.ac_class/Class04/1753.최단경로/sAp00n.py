from sys import stdin
import heapq


V, E = map(int, stdin.readline().split())
graph = {i: [] for i in range(1, V + 1)}
K = int(stdin.readline())

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

que = []
result = ['INF'] * V
result[K - 1] = 0
heapq.heappush(que, (0, K))

# print(graph)
while que:
    distance_from_root, current_node = heapq.heappop(que)
    for link_data in graph[current_node]:
        linked_node, distance_from_current = link_data
        if result[linked_node - 1] == 'INF' or result[linked_node - 1] > distance_from_current + distance_from_root:
            result[linked_node - 1] = distance_from_current + distance_from_root
            heapq.heappush(que, (distance_from_current + distance_from_root, linked_node))

for total_distance in result:
    print(total_distance)

