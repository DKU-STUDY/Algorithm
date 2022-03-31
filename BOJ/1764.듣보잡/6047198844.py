import sys
from collections import Counter

N, M = map(int, input().split())
names = [sys.stdin.readline().rstrip() for _ in range(N + M)]
count_names = Counter(names)
res = list(filter(lambda names: count_names[names] == 2, Counter(names).keys()))
res.sort()
print(len(res))
for i in res:
    print(i)