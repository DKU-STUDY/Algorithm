
def dfs(v):
    print(v, end=" ")
    visited[v]= True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

from collections import deque

def bfs(v):
    q= deque([v])

    while q:
        v= q.popleft()
        if not visited[v]:
            visited[v]= True
            print(v, end=" ")
            for i in adj[v]:
                if not visited[i]:
                    q.append(i)

# n, m, v 입력
n, m, v= map(int, input().split())

# 간선 입력
adj =[[] for i in range(n+1)]

for i in range(m):
    x, y= map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
# print(adj)

for i in adj:
    i.sort()
# print(adj)

visited= [False] * (n+1)
dfs(v)
print()
visited= [False] * (n+1)
bfs(v)