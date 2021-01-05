from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1
    node_cnt=1
    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+dx, y+dy

            # x, y값이 범위 내에 있으며 방문하지 않았고, 입력 값이 1이라면 q에 넣고, 방문 처리하고, 노드의 수를 count
            if 0<=tmp_x<n and 0<= tmp_y< n and not visited[tmp_x][tmp_y] and adj[tmp_x][tmp_y]==1:
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y]= 1
                node_cnt+=1

    return node_cnt


n= int(input())

adj= [[] for _ in range(n)]
visited= [[0 for _ in range(n)] for _ in range(n)]
cnt=[]
tmp= 0

for i in range(n):
    adj[i]=list(map(int, list(str(input()))))

# for i in range(n):
#     print(adj[i])

# 방문하지 않았으며 입력 값이 1인 경우에 bfs 실행
for i in range(n):
    for j in range(n):
        if not visited[i][j] and adj[i][j]== 1:
            # print(i, j)
            tmp= bfs([i, j])
            cnt.append(tmp)
cnt.sort()

# 출력 부분
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
