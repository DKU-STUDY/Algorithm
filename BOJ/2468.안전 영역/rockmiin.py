from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1

    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tx, ty= x+ dx, y+ dy
            if 0<= tx< n and 0<= ty< n:
                if adj[tx][ty] > h and not visited[tx][ty]:
                    q.append([tx, ty])
                    visited[tx][ty]= 1

n= int(input())
adj=[list(map(int, input().split())) for _ in range(n)]
res= 0
height= 0

for i in range(n):
    for j in range(n):
        if adj[i][j]> height: height= adj[i][j]

# print("height :", height)
for h in range(height):
    cnt= 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
                if not visited[i][j] and adj[i][j]> h:
                    bfs([i, j])
                    cnt += 1
                    if visited[i][j]==0: cnt= 0; continue;
    res= max(res, cnt)
print(res)

# 시간복잡도를 계산할 때 높이가 1이상 100이하라는 작은 범위였기 때문에 완전탐색이 가능했다.

