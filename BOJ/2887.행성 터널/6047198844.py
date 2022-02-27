import heapq
import math
import sys
from collections import deque

N = int(sys.stdin.readline())
x_vertexes = []
y_vertexes = []
z_vertexes = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    x_vertexes.append((x, i))
    y_vertexes.append((y, i))
    z_vertexes.append((z, i))

edges = []

x_vertexes.sort()
y_vertexes.sort()
z_vertexes.sort()

for i in range(1, N):
    x1, V = x_vertexes[i]
    x2, W = x_vertexes[i - 1]
    edges.append((abs(x1 - x2), V, W))

    y1, V = y_vertexes[i]
    y2, W = y_vertexes[i - 1]
    edges.append((abs(y1 - y2), V, W))

    z1, V = z_vertexes[i]
    z2, W = z_vertexes[i - 1]
    edges.append((abs(z1 - z2), V, W))

edges.sort()

P = [i for i in range(N)]


def union(V, W):
    PV = find(V)
    PW = find(W)

    if PV == PW:
        return False

    P[PW] = PV
    return True


def find(V):
    if P[V] == V:
        return P[V]
    P[V] = find(P[V])
    return P[V]

res = 0
for dist, V, W in edges:
    if not union(V, W):
        continue
    res += dist
print(res)