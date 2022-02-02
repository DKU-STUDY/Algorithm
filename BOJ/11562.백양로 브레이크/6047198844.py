import sys

n, m = map(int, sys.stdin.readline().split())
roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
buildings = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            buildings[i][j] = 987654321

for u, v, b in roads:
    buildings[u - 1][v - 1] = 0
    buildings[v - 1][u - 1] = int(b == 0)

for k in range(n):
    for i in range(n):
        for j in range(n):
            buildings[i][j] = min(buildings[i][j], buildings[i][k] + buildings[k][j])

k = int(sys.stdin.readline())
for _ in range(k):
    s, e = map(int, sys.stdin.readline().split())
    print(buildings[s-1][e-1])
