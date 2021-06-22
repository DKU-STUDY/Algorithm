#최소 스패닝 트리
#연결할 수 없는 섬은 주어지지 않습니다.
import heapq
from collections import defaultdict

def solution(n, costs):
    answer = 0
    
    graph = defaultdict(list)
    
    for i, j, k in costs:
        graph[i].append((k, j))
        graph[j].append((k, i))
    
    #prim 알고리즘
    #선택된 정점. 시작정점 0
    selected = set([0])
    edges = []
    for k, j in graph[0]:
        heapq.heappush(edges,(k,j))
    
    while edges:
        cost, i = heapq.heappop(edges)
        if i not in selected:
            selected.add(i)
            for k, j in graph[i]:
                heapq.heappush(edges,(k,j))
            answer += cost
        
    return answer