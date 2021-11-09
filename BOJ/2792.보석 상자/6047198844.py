import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
colors = []
for _ in range(M):
    marble = int(sys.stdin.readline().rstrip())
    heapq.heappush(colors, (-marble, marble))

for _ in range(N-M):
    max_color = heapq.heappop(colors)[1]
    heapq.heappush(colors, (-(max_color // 2 + max_color % 2), max_color // 2 + max_color % 2))
    heapq.heappush(colors, (-(max_color // 2), max_color // 2))


print(heapq.heappop(colors)[1])