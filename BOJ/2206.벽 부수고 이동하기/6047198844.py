import collections

#0은 이동할수있는 곳. 1은 이동할수없는 벽이 있는 곳을 나타낸다.
#0,0은 항상 0이다.
#N-1,M-1은 항상 0이다.
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
#벽을 부술수있는지 여부, 현재 좌표
#벽을 부숴서 움직였을때 해당 좌표가 유효한지 판단

Q = collections.deque()
discovered = set()
Q.append((True, 0, 0))
discovered.add((True, 0, 0))

distance_cnt = 1
#예외처리 N, M이 1, 1 인경우
#정답은 1칸이다. 문제에서 요구하는건 맵에서 가장 적은 개수의 칸을 지나는 경로이다.
if N == M == 1:
    print(distance_cnt)
    exit()

while Q:
    distance_cnt += 1
    for _ in range(len(Q)):
        breakable, y, x = Q.popleft()
        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            #이동한다.
            ny = y + dy
            nx = x + dx
            #범위에 도달하는지 확인한다.
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            #답인 경우 출력한다.
            if ny == N - 1 and nx == M - 1:
                print(distance_cnt)
                exit()
            #이동할 장소가 벽인 경우
            if board[ny][nx] == '1':
                #벽을 부술수있는 기회가 남아 있고, 그리고 발견되지 않은 상황인경우.
                #벽을 부술수있다는것은 유리한 상황이다.
                #벽에 위치한 상태는 항상 not breakable이다.
                if breakable and (not breakable, ny, nx) not in discovered:
                    discovered.add((not breakable, ny, nx))
                    Q.append((not breakable, ny, nx))

            #이동할 거리가 벽이 아닌 경우
            elif (breakable, ny, nx) not in discovered:
                discovered.add((breakable, ny, nx))
                Q.append((breakable, ny, nx))
#벽 부수기로 갈수없는 경우
print(-1)