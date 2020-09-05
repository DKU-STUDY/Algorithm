from collections import deque

def solution(n, computers):
    answer=0
    visited = [0] * (n + 1)
    arr = [[] for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                arr[i+1].append(j+1)
    # print(arr)

    def bfs(v):
        q=deque([v])

        while q:
           k= q.popleft()
           if not visited[k]:
                visited[k]=1
                for e in arr[k]:
                    if not visited[e]:
                        q.append(e)
                        
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i); answer+=1

    return answer

print(
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
)
