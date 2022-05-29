import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
P = [i for i in range(n * m)]


def union(A, B):
    PA = find(A)
    PB = find(B)

    if PA == PB:
        return

    P[PA] = PB


def find(A):
    if A == -1 or A == P[A]:
        return A
    P[A] = find(P[A])
    return P[A]


for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            P[m * y + x] = -1
            continue

        for ny, nx in (y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1):
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                A = m * y + x
                B = m * ny + nx
                union(A, B)

dictionary = defaultdict(int)
for i in P:
    dictionary[find(i)] += 1

res_n = 0
res_area = 0
for key, value in dictionary.items():
    if key == -1:
        continue
    res_n += 1
    res_area = max(res_area, value)

print(res_n)
print(res_area)