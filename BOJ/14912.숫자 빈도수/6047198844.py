import sys
from collections import Counter

n, d = map(int, sys.stdin.readline().split())
counter = Counter()
for i in range(1, n + 1):
    counter += Counter(str(i))
print(counter.get(str(d)))