from collections import deque

test_case= int(input())
move= [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

def bfs(v):
    q= deque([v])
    while q:
        x, y= q.popleft()

        if x== end_x and y== end_y:
            return visited[x][y]
        for dx, dy in move:
            tmp_x, tmp_y= x+ dx, y+ dy
            if 0<= tmp_x< n and 0<= tmp_y< n and not visited[tmp_x][tmp_y]:
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y]= visited[x][y]+1


for i in range(test_case):

    n= int(input())
    start_x, start_y= map(int, input().split())
    end_x, end_y= map(int, input().split())
    visited=[[0 for _ in range(n)] for _ in range(n)]

    print(bfs([start_x, start_y]))

# 각 test_case마다 변수들을 새로 지정해줘서
# depth와 방문 여부를 확인하는 visited 리스트를 생성해준다.
# 종료 지점과 일치하는 좌표가 q에서 나오게 되면 depth를 리턴해주는 방식으로 구현

# 예제 입력
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
#
# 예제 출력
# 5
# 28
# 0