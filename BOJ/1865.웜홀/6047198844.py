import heapq
import math
import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T))

    dist = [987654321 for _ in range(N+1)]
    for _ in range(N-1):
        for S, E, T in edges:
            if dist[E] > dist[S] + T:
                dist[E] = dist[S] + T

    for S, E, T in edges:
        if dist[E] > dist[S] + T:
            print('YES')
            break
    else:
        print('NO')

