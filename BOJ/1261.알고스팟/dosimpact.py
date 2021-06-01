import sys
import math
from typing import *
import itertools
from collections import deque


# 알고스팟
# N,M 빈방 - 가중치 0, 벽 1

M, N = map(int, input().split())
graph: List[List[int]] = [list(map(int, list(input()))) for _ in range(N)]
check: List[List[int]] = [[-1 for _ in range(M)] for _ in range(N)]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()
q.append((0, 0))  # 0,0 으로 들어옴
check[0][0] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if inRange(nx, ny) and check[nx][ny] == -1:
            if graph[nx][ny] == 0:
                check[nx][ny] = check[x][y]
                q.appendleft((nx, ny))
                continue
            if graph[nx][ny] == 1:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))
                continue

print(check[N-1][M-1])
