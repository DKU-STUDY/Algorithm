from sys import stdin
import heapq


N = int(stdin.readline())

max_heap = []

for _ in range(N):
    x = int(stdin.readline())
    if x != 0:
        heapq.heappush(max_heap,-x)
    elif x == 0 and len(max_heap) > 0:
        print(-heapq.heappop(max_heap))
    else:   print(0)


