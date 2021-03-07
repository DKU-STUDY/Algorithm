from collections import deque

def bfs(q):
    global res

    tmp= deque()
    while q:
        x, y= q.popleft()

        if visited[x][y]==0 :
            visited[x][y]= 1

        if adj[x][y]== '*':
            continue

        if x== end[0] and y==end[1]:
            # print(visited[x][y]);
            res= visited[x][y]; break;
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy

            # 범위 내에 있고 방문하지 않고, ., D인 경우에 tmp에 넣어주고 return
            if 0<= tmp_x< r and 0<= tmp_y< c and not visited[tmp_x][tmp_y]:
                if adj[tmp_x][tmp_y]== '.' or adj[tmp_x][tmp_y]== 'D' and adj[x][y]!='*':
                    tmp.append([tmp_x, tmp_y])
                    visited[tmp_x][tmp_y]= visited[x][y]+ 1
    return tmp


def water_bfs(q):
    tmp= deque()

    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy
            if 0<= tmp_x< r and 0<= tmp_y< c and adj[tmp_x][tmp_y]!= '*':
                if adj[tmp_x][tmp_y]!= 'D' and adj[tmp_x][tmp_y]!='X':
                    tmp.append([tmp_x, tmp_y])
                    adj[tmp_x][tmp_y]= '*'
    return tmp

r, c= map(int, input().split())
adj= []
res= 0

for i in range(r):
    adj.append(list(input()))

water= deque()
now= deque()

for i in range(r):
    for j in range(c):
        if adj[i][j]== 'D':
            end= [i, j]
        elif adj[i][j]== 'S':
            now.append([i, j])
        elif adj[i][j]== '*':
            water.append([i, j])

visited=[[0 for _ in range(c)] for _ in range(r)]

while now:
    now= bfs(now)
    water= water_bfs(water)
    # print("n", now)
    # print("w", water)
    if res !=0: print(res-1); break;
if res==0: print('KAKTUS')