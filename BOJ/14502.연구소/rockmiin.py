from collections import deque
import copy
import time

# st= time.time()
def bfs():
    # 함수 안에서 전역 변수의 값을 변경하려면 global 키워드를 사용
    global res

    # adj, real_q값을 변경하면 안되니까 깊은 복사를 사용하여 구현
    adj_copy= copy.deepcopy(adj)
    # q= copy.deepcopy(real_q)
    cnt= 0

    q = deque()
    for i in range(n):
        for j in range(m):
            if adj[i][j] == 2:
                q.append([i, j])

    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tmp_x, tmp_y= x+ dx, y+ dy
            if 0<= tmp_x< n and 0<= tmp_y< m and adj_copy[tmp_x][tmp_y]==0:
                adj_copy[tmp_x][tmp_y]= 2
                q.append([tmp_x, tmp_y])

    # adj_copy 값이 바이러스가 다 퍼졌을 시 확인
    # for i in adj_copy:
    #     print(i)
    # print()

    # adj_copy에서 0의 개수가 res 값보다 크면 change
    for i in range(n):
        for j in range(m):
            if adj_copy[i][j]==0:
                cnt+=1

    res= max(res, cnt)

def search_wall(cnt):

    if cnt==3:
        # for i in adj:
        #     print(i)
        # print()
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if adj[i][j]== 0:
                # 모든 경우의 수를 다 돌고 0으로 바꿔준다 다시
                adj[i][j]= 1
                search_wall(cnt+1)
                adj[i][j]= 0



n, m= map(int, input().split())
adj= []
res= 0

for i in range(n):
    adj.append(list(map(int, input().split())))

# 바이러스가 있는 위치를 real_q에 담아놓음음
# real_q=deque()
# for i in range(n):
#     for j in range(m):
#         if adj[i][j]== 2:
#             real_q.append([i, j])
# for i in adj:
#     print(i)
# print()

search_wall(0)
print(res)

# print("time :", time.time()-st)
# 입력 예시
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 출력 예시
# 9