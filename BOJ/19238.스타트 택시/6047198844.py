import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cur_pos = tuple(map(lambda i: int(i) - 1, sys.stdin.readline().split()))

customers = dict()
for _ in range(M):
    iy, ix, jy, jx = map(lambda i: int(i) - 1, sys.stdin.readline().split())
    customers[(iy, ix)] = (jy, jx)

# 반복문 조건 : 연료가 0이상, 손님이 있어야 한다.
while K >= 0 and customers:
    # 고객을 찾는다.
    # 방문한곳은 다시 방문하지 않는다.
    visited = set()
    visited.add(cur_pos)
    Q = deque()
    Q.append(cur_pos)

    shortest_customers = list()
    # 현재 위치에 손님이 있는 경우.
    if cur_pos in customers:
        shortest_customers.append(cur_pos)

    fuel = 0

    # 현재위치에 손님이 위치할때까지 찾는다.
    while Q and not shortest_customers:
        fuel += 1
        for _ in range(len(Q)):
            cur_y, cur_x = Q.popleft()
            for ny, nx in (cur_y - 1, cur_x), (cur_y + 1, cur_x), (cur_y, cur_x - 1), (cur_y, cur_x + 1):
                if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited and board[ny][nx] == 0:
                    Q.append((ny, nx))
                    visited.add((ny, nx))
                    if (ny, nx) in customers:
                        shortest_customers.append((ny, nx))
    # 손님이 존재한다면
    if shortest_customers:
        shortest_customers.sort()
        cur_pos = shortest_customers[0]  # 현재 승객위치. 단 이 승객은 row / column 이 가장 작은 승객이다.
        K -= fuel # 연료를 소모한다.

        # 도착 위치
        target_y, target_x = customers.get(cur_pos)
        TQ = deque()
        TQ.append(cur_pos)

        target_visited = set()
        target_visited.add(cur_pos)
        is_arrived = False
        target_fuel = 0

        # 도착 위치까지 최단 거리로 이동
        while TQ and (not is_arrived):
            target_fuel += 1
            for _ in range(len(TQ)):
                cur_y, cur_x = TQ.popleft()
                for ny, nx in (cur_y - 1, cur_x), (cur_y + 1, cur_x), (cur_y, cur_x - 1), (cur_y, cur_x + 1):
                    if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in target_visited and board[ny][nx] == 0:
                        TQ.append((ny, nx))
                        target_visited.add((ny, nx))
                        if (ny, nx) == (target_y, target_x):
                            is_arrived = True
        # 도착하면 일단 연료를 깎는다.
        if is_arrived:
            K -= target_fuel
        # 도착하지 못하면 끝이다.
        else:
            break

        # 2배 연료 충전.
        if K >= 0:
            K += 2 * target_fuel
        # 연료가 없을 경우. 끝이다.
        else:
            break

        # 승객을 제거. 현재 위치를 이동시킨다.
        customers.pop(shortest_customers[0])
        cur_pos = (target_y, target_x)

    # 손님을 하나도 못태운 경우
    else:
        break

# 연료가 0 이상인데, 손님이 없는 경우
if K >= 0 and not customers:
    print(K)
# 연료가 0 미만인 경우. 손님 유무와 상관없이 -1 / 연료가 있지만 손님도 있는 경우.
else:
    print(-1)
