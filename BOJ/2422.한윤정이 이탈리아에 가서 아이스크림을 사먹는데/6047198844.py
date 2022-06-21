from collections import defaultdict
from itertools import combinations

N, M = map(int, input().split())

not_allowed = defaultdict(set)
for _ in range(M):
    A, B = map(int, input().split())
    not_allowed[A].add(B)
    not_allowed[B].add(A)

res = 0
for i in combinations(range(1, N + 1), 3):
    for j in i:
        if not_allowed[j].intersection(i):
            break
    else:
        res += 1
print(res)