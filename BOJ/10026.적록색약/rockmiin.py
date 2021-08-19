from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1

    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+dx, y+dy

            if 0<= tmp_x< n and 0<= tmp_y< n and adj[x][y]==adj[tmp_x][tmp_y] and visited[tmp_x][tmp_y]==0:
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y]=1

def bfs_rg(v):
    q= deque([v])
    visited_rg[v[0]][v[1]]= 1

    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+dx, y+dy

            if 0 <= tmp_x < n and 0 <= tmp_y < n and visited_rg[tmp_x][tmp_y]==0:

                if adj[x][y]== adj[tmp_x][tmp_y]:
                    q.append([tmp_x, tmp_y])
                    visited_rg[tmp_x][tmp_y] = 1

                elif adj[tmp_x][tmp_y] in rg and adj[x][y] in rg:
                    q.append([tmp_x, tmp_y])
                    visited_rg[tmp_x][tmp_y] = 1



n= int(input())
rg= ['R', 'G']
adj= []
visited= [[0 for _ in range(n)] for _ in range(n)]
visited_rg= [[0 for _ in range(n)] for _ in range(n)]

cnt= 0
cnt_rg= 0
for i in range(n):
    adj.append(list(input()))

# for i in adj:
#     print(i)
# print()

for i in range(n):
    for j in range(n):

        if visited[i][j]== 0:
            bfs([i, j])
            cnt+=1

        if visited_rg[i][j]== 0:
            bfs_rg([i, j])
            cnt_rg+=1

print(cnt, cnt_rg)

# 일반인의 경우에는 기존에 사용하던 BFS 방식으로 구현을 하였으며,
# 색약인 사람의 경우 인접한 color가 red, green인 경우에는 같은 구역의 q로 append 해줌으로써 구현

# 예제 입력
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
#
# 예제 출력
# 4 3