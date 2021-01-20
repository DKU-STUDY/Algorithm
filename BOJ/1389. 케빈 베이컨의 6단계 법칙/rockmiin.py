from collections import deque

def bfs(start, end):
    q= deque([start])
    visited = [0] * (n+1)
    visited[start]= 1

    while q:
        x= q.popleft()

        if x==end: return visited[end]-1

        for i in adj[x]:
            if not visited[i]:
                q.append(i)
                visited[i]= visited[x]+1

n, m= map(int, input().split())
res= [0]
adj=[[] for _ in range(n+1)]
for i in range(m):
    x, y= map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# print(adj)

for i in range(1, n+1):
    cnt= 0
    for j in range(1, n+1):
        cnt+=bfs(i, j)
    res.append(cnt)
print(res.index(min(res[1:])))
