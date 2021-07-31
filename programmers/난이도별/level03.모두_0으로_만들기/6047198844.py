import collections
import sys
sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    #global answer
    answer = 0
    graph = collections.defaultdict(list)
    visited = set()
    
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    def dfs(vertex):
        visited.add(vertex)
        W = 0
        for neigh in graph[vertex]:
            if neigh not in visited:
                W += dfs(neigh)
        #W는 위에서 올라온것. 즉 이동이 이루어진것이다.
        nonlocal answer
        W += a[vertex]
        answer = answer + abs(W)

        return W
    
    return answer if dfs(0) == 0 else -1
    '''
    for v in range(len(a)):
        Q = [v]
        level = -1
        while Q and a[v] < 0:
            level += 1
            for _ in range(len(Q)):
                neigh = Q.pop(0)
                if neigh != v and a[neigh] > 0:
                    if a[neigh] >= -a[v]:
                        a[neigh] += a[v]
                        answer += -a[v] * level
                        a[v] = 0
                        break
                    else:
                        a[v] += a[neigh]
                        answer += a[neigh] * level
                        a[neigh] = 0
                for nv in graph[neigh]:
                    Q.append(nv)
                    
        if a[v] != 0:
            return -1
        
    
    return answer
    '''