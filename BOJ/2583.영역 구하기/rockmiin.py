from collections import deque

def bfs(v):
    q= deque([v])
    area[v[0]][v[1]]= 1
    count= 1
    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy
            if 0<= tmp_x< m and 0<= tmp_y< n and area[tmp_x][tmp_y]==0:
                q.append([tmp_x, tmp_y])
                area[tmp_x][tmp_y]= 1
                count+=1
    return count
    # print(count)
    # for i in area:
    #     print(i)


m, n, k= map(int, input().split())

# m이 세로, n이 가로
area= [[0 for _ in range(n)] for _ in range(m)]
cnt= []

# 블록 색칠
for i in range(k):
    x1, y1, x2, y2= list(map(int, input().split()))

    for j in range(y1, y2):
        # slicing할 떄 주의점 좌 우의 개수를 맞춰줘야 함
        area[j][x1:x2]=[2]*(x2-x1)
    # for i in area:
    #     print(i)

for i in range(m):
    for j in range(n):
        if area[i][j]==0:
            cnt.append(bfs([i, j]))

print(len(cnt))
for i in (sorted(cnt)):
    print(i, end=" ")


# 입력
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

# 출력
# 3
# 1 7 13