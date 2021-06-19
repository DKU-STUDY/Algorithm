import collections
import heapq

def solution(N, roads, K):
    answer = 0
    
    graph = collections.defaultdict(list)
    for road in roads:
        i, j, cost = road
        graph[i].append((j,cost))
        graph[j].append((i,cost))
    
    Q = []
    heapq.heappush(Q,(0,1))
    distance = collections.defaultdict(int)
    
    while Q:
        time, node = heapq.heappop(Q)
        if time > K:
            break
        
        if node not in distance:
            distance[node] = time
            for k, v in graph[node]:
                alt = time + v
                heapq.heappush(Q,(alt,k))
    
    return len(distance)