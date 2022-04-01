import math
import sys

N = int(sys.stdin.readline())
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if distance[y][x] == 0:
            distance[y][x] = math.inf

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for y in range(N):
    for x in range(N):
        if distance[y][x] != math.inf:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()