import sys
from bisect import bisect_right
from collections import deque

N = int(sys.stdin.readline())
wires = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
wires.sort()
memo = []
idx_memo = []
for wire in wires:
    left, right = wire
    idx = bisect_right(memo, right)
    if idx == len(memo):
        memo.append(right)
    else:
        memo[idx] = right
    idx_memo.append(idx)

print(len(wires) - len(memo))

i = len(memo) - 1
j = len(idx_memo) - 1
res = []
while j >= 0:
    if idx_memo[j] == i:
        i -= 1
    else:
        res.append(wires[j][0])
    j -= 1
for i in res[::-1]:
    print(i)