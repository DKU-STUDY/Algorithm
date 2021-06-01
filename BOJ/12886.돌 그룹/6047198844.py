import collections
from itertools import combinations

A, B, C = map(int, input().split())
Q = collections.deque()
discovered = set()
Q.append((A, B, C))
discovered.add((A, B, C))
while Q:
    a, b, c = Q.popleft()
    if a == b == c:
        print(1)
        exit()

    if a != b:
        if a < b:
            na = a + a
            nb = b - a
        else:
            nb = b + b
            na = a - b
        if (na, nb, c) not in discovered:
            discovered.add((na, nb, c))
            Q.append((na, nb, c))

    if a != c:
        if a < c:
            na = a + a
            nc = c - a
        else:
            nc = c + c
            na = a - c
        if (na, b, nc) not in discovered:
            discovered.add((na, b, nc))
            Q.append((na, b, nc))

    if b != c:
        if b < c:
            nb = b + b
            nc = c - b
        else:
            nc = c + c
            nb = b - c
        if (a, nb, nc) not in discovered:
            discovered.add((a, nb, nc))
            Q.append((a, nb, nc))

print(0)
