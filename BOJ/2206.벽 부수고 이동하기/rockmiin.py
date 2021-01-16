from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]][0]= 1
    while q:

        x, y= q.popleft()

        for i in visited:
            print(i)
        print()
        # print(x, y, visited[x][y][1])
        if x==n-1 and y==m-1:
            # for i in visited:
            #     print(i)
            return visited[x][y][0]

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy

            if 0<= tmp_x< n and 0<= tmp_y< m and adj[tmp_x][tmp_y]== 0 and not visited[tmp_x][tmp_y][0]:
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y][0]= visited[x][y][0] +1 # 방문처리
                visited[tmp_x][tmp_y][1]= visited[x][y][1] # 부모의 벽 부신 유무 따라감

            if 0<= tmp_x<n and 0<= tmp_y< m and adj[tmp_x][tmp_y]== 1 and visited[x][y][1]== 0 and not visited[tmp_x][tmp_y][0]:
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y][0]= visited[x][y][0] +1
                visited[tmp_x][tmp_y][1]= 1
    if visited[n-1][m-1][0]== 0:
        return -1

n, m= map(int, input().split())
adj= [list(map(int, input())) for _ in range(n)]

# 각 노드마다 visited[x][y][0]에는 방문 여부와 최단거리, visited[x][y][1]에는 벽을 부섰는지의 여부가 들어간다.
visited= [[[0, 0] for _ in range(m)] for _ in range(n)]
res= bfs([0, 0])
print(res)

