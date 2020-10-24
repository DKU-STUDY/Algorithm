from sys import stdin
import heapq

min_heap = []

N = int(stdin.readline())

for _ in range(N):
    input_val = int(stdin.readline())
    if input_val == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, input_val)