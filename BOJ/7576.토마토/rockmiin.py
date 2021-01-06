import sys

def bfs(q):
    tmp= []
    # print(q)
    while q:
        x, y= q.pop(0)
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy
            if 0<=tmp_x<n and 0<=tmp_y<m and not visited[tmp_x][tmp_y] and adj[tmp_x][tmp_y]==0:
                tmp.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y]= 1
                adj[tmp_x][tmp_y]= 1
    return tmp


m, n= map(int, sys.stdin.readline().split())

adj=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]
tomato= []
cnt= -1
# for i in adj:
#     print(i)

for i in range(n):
    for j in range(m):
        if adj[i][j]== 1:
            tomato.append([i, j])

while tomato:
    tomato= bfs(tomato)
    cnt+=1

# for i in adj:
#     print(i)
for i in range(n):
    for j in range(m):
        if adj[i][j]==0:
            cnt= -1; break

print(cnt)
