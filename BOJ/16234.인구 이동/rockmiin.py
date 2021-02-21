from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1
    area= [v]
    sum_value= adj[v[0]][v[1]]
    while q:
        x, y= q.popleft()
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tx, ty= x+ dx, y+ dy
            if 0<=tx <n and 0<= ty< n:
                if l<= abs(adj[tx][ty]- adj[x][y])<=r and not visited[tx][ty]:
                    q.append([tx, ty])
                    area.append([tx, ty])
                    sum_value+=adj[tx][ty]
                    visited[tx][ty]= 1
    return area, sum_value

n, l, r= map(int, input().split())
adj= [list(map(int, input().split())) for _ in range(n)]
cnt= 0; res= []
while True:
    # 이걸 할 때마다 count해서 값 도출
    visited=[[0]*n for _ in range(n)]
    res, cum= [], []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmp, tmp_sum =bfs([i, j])
                if len(tmp)!=1:
                    res.append(tmp)
                    cum.append(tmp_sum)
    if res==[]:
        break;

    for i in range(len(res)):
        avg= cum[i]//len(res[i])
        for j in res[i]:
            adj[j[0]][j[1]]= avg
    cnt+=1

    # for i in adj:
    #     print(i)
    # print()
print(cnt)
