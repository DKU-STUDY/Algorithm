from collections import deque

def bfs(v):
    q= deque([v])
    visited[0][0]= 1 # 초기 값 설정
    while q:
        x, y= q.popleft()
        # print(q)
        if x==n-1 and y==m-1: return visited[x][y] # n, m의 위치에 도달했을 때 return
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]: # 상하좌우 이동
            tmp_x, tmp_y= x+dx, y+dy

            if 0<=tmp_x<n and 0<=tmp_y<m and arr[tmp_x][tmp_y]==1: # 미로의 크기 내에 있고, 갈 수 있는 곳으로

                if not visited[tmp_x][tmp_y]: # 방문한 노드는 재방문 하지 않도록 설정
                    # print(tmp_x, tmp_y)
                    q.append([tmp_x, tmp_y])
                    visited[tmp_x][tmp_y]= visited[x][y]+1



n, m= map(int, input().split())

arr= [[0]* (m) for _ in range(n)]
for i in range(n):
    k = list(map(int, list(str(input()))))
    for j in range(m):

        arr[i][j]=k[j]

# print(arr)

visited=[[0]* (m) for _ in range(n)]
print(bfs([0, 0]))

# for i in range(n):
#     print(visited[i])

# 입력 예시
# 4 6
# 101111
# 101010
# 101011
# 111011

# 출력 예시
# 15
