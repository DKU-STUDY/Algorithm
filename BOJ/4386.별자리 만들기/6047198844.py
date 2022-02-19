import heapq
import sys

sys.setrecursionlimit(10 ** 7)


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return
    P[PB] = PA


def find(A):
    if P[A] == -1:
        return A
    P[A] = find(P[A])
    return P[A]


n = int(sys.stdin.readline())
P = [-1 for _ in range(n)]
V = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    V.append((x, y))

Q = []
for i in range(n):
    for j in range(i + 1, n):
        ix, iy = V[i]
        jx, jy = V[j]

        heapq.heappush(Q, (((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5, i, j))

res = 0
while Q:
    cost, v, w = heapq.heappop(Q)
    pv = find(v)
    pw = find(w)
    if pv == pw:
        continue
    union(v, w)
    res += cost
print(round(res, 2))
