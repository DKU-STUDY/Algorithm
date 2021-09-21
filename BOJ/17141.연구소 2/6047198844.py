"""
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
"""
from collections import deque
from itertools import combinations


def flood_fill(board, visited, V):
    Q = deque(visited)
    time = -1

    while Q:
        for _ in range(len(Q)):
            y, x = Q.popleft()
            for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and (board[ny][nx] == 0 or board[ny][nx] == 2) \
                        and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    Q.append((ny, nx))
        time += 1
    return time if len(visited) == V else -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
min_time = -1

# visited 위치를 찾자
# V는 virus 를 넣어야하는 개수이다.
virus = list()
V = 0
for y in range(N):
    for x in range(N):
        if board[y][x] != 1:
            if board[y][x] == 2:
                virus.append((y, x))
            V += 1

# start == ((0,0), (3,6), (6,0))
# virus 에서 M개를 뽑는다.
for start in combinations(virus, M):
    visited = set(start)
    time = flood_fill(board, visited, V)
    if time != -1 and (min_time == -1 or min_time > time):
        min_time = time

print(min_time)
