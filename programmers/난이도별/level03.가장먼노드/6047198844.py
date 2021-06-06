#1부터 n까지 번호가 적혀있다.
#1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하는것.
#BFS?
import collections
def solution(n, edge):
    #graph작성
    graph = collections.defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    Q = [1]
    discovered = set()
    discovered.add(1)
    
    n = 0
    while Q:
        n = len(Q)
        for _ in range(n):
            node = Q.pop(0)
            for v in graph[node]:    
                if not v in discovered:
                    discovered.add(v)
                    Q.append(v)
    answer = n
    return answer