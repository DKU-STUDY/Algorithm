from collections import deque

move= [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

def bfs(q):
    while q:
        z, y, x= q.popleft()

        for dx, dy, dz in move:
            tx, ty, tz= x+ dx, y+ dy, z+ dz

            if 0<= tx< m and 0<= ty< n and 0<= tz< h:
                if adj[tz][ty][tx]==0 and not visited[tz][ty][tx]:
                    q.append([tz, ty, tx])
                    adj[tz][ty][tx]= 1
                    visited[tz][ty][tx]= visited[z][y][x]+ 1

    res= 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if adj[i][j][k]== 0:
                    return -1
                if visited[i][j][k]> res:
                    res= visited[i][j][k]
    return res-1

m, n, h= map(int, input().split())
adj= []
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

for i in range(h):
    tmp= []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    adj.append(tmp)

tomato= deque()
cnt= 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if adj[i][j][k]==1:
                tomato.append([i, j, k])
                visited[i][j][k]= 1

print(bfs(tomato))


