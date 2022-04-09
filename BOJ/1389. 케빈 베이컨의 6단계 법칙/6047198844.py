import math
import sys

N, M = map(int, sys.stdin.readline().split())
distance = [[math.inf for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        if y == x:
            distance[y][x] = 0

for _ in range(M):
    i, j = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    distance[i][j] = 1
    distance[j][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

res = list(map(sum, distance))
print(res.index(min(res)) + 1)