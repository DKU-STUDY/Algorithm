import sys

n = int(input())
bars = list(map(int, sys.stdin.readline().split()))
res = 0
s = sum(bars)
for bar in bars:
    res += bar * (s - bar)
    s -= bar
print(res)