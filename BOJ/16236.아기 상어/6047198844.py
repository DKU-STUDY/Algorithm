import sys

#
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
#
# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
#
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
from collections import deque

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# BFS
# 물고기를 먹는다.
# 물고기를 먹는 조건
# 자신 보다 작아야함.
# 자신 보다 크면 지나갈수없음.
# 같으면 지나갈수있는데 먹을수는 없음.
# 거리가 같으면 맨위, 맨위도 같으면 맨 왼쪽을 먹음
# 자신만큼 먹었으면 크기가 커짐.

# 먹은 상어의 좌표와 걸린 시간을 반환.
def bfs(sy, sx, size):
    Q = deque([(sy, sx)])
    visited = set()
    visited.add((sy, sx))
    catch = []
    cnt = 0
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            y, x = Q.popleft()
            # 상하좌우 탐색
            for ny, nx in (y+1, x), (y, x+1), (y-1, x), (y, x-1):
                # 범위 벗어난 경우. 방문한경우
                if not (0 <= ny < N and 0 <= nx < N) or (ny, nx) in visited:
                    continue
                # 빈칸인 경우
                if arr[ny][nx] == 0:
                    Q.append((ny, nx))
                    visited.add((ny, nx))
                # 크키가 큰 물고기인경우
                elif arr[ny][nx] > size:
                    continue
                # 크기가 같은 물고기인 경우
                elif arr[ny][nx] == size:
                    Q.append((ny, nx))
                    visited.add((ny, nx))
                # 크기가 작은 물고기인 경우, 큐에는 굳이 넣지않음.
                else:
                    catch.append((ny, nx))
                    visited.add((ny, nx))

        # 잡은 물고기가 있음?
        if catch:
            # 맨위, 맨좌 물고기뽑음
            return cnt, min(catch)

    # 잡은 물고기가 없음.
    return None, (None, None)


fishes = []
for y in range(N):
    for x in range(N):
        if arr[y][x] != 0:
            if arr[y][x] == 9:
                shark = (y, x)
            else:
                fishes.append((y, x))

sy, sx = shark
shark_size = 2
fish_cnt = 0
res = 0

while True:
    # 물고기를 잡는데 든 시간, 잡은 물고기 위치
    t, (ny, nx) = bfs(sy, sx, shark_size)
    if t is None:
        print(res)
        break

    # 물고기 잡음
    res += t
    fish_cnt += 1
    arr[sy][sx] = 0
    arr[ny][nx] = 9
    sy, sx = ny, nx

    if fish_cnt == shark_size:
        fish_cnt = 0
        shark_size += 1