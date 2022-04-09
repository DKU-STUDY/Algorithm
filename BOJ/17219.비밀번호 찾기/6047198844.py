import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
table = defaultdict(str)
for _ in range(N):
    key, value = sys.stdin.readline().split()
    table[key] = value

for _ in range(M):
    key = sys.stdin.readline().rstrip()
    print(table[key])