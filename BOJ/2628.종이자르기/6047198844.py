import math
import sys

width, height = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

cut_width = list()
cut_height = list()

for _ in range(N):
    i, j = map(int, sys.stdin.readline().split())
    if i == 0:
        cut_height.append(j)
    else:
        cut_width.append(j)

cut_height.append(0)
cut_height.append(height)

cut_width.append(0)
cut_width.append(width)

cut_width.sort()
cut_height.sort()

res = -math.inf
for i in range(len(cut_height) - 1):
    for j in range(len(cut_width) - 1):
        res = max(res, (cut_height[i+1] - cut_height[i]) * (cut_width[j+1] - cut_width[j]))
print(res)