from collections import deque

def bfs(start, end):
    q= deque([start])
    while q:
        v= q.popleft()

        if v== end: break;

        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                visited[i]= visited[v]+1

    if visited[end]==0:
        return -1

    return visited[end]

n= int(input())
start, end= map(int, input().split())
m= int(input())

adj= [[] for _ in range(n+1)]

for i in range(1, m+1):
    x, y= map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in adj:
    i.sort()

# print(adj)

visited = [0 for _ in range(n + 1)]

print(bfs(start, end))
