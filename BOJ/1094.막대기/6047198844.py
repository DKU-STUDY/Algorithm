import heapq
import sys

X = int(sys.stdin.readline())

S = 64
sticks = [64]
while S > X:
    if S > X:
        stick = heapq.heappop(sticks)
        heapq.heappush(sticks, stick // 2)
        heapq.heappush(sticks, stick // 2)

        if S - sticks[0] >= X:
            heapq.heappop(sticks)
            S -= sticks[0]
print(len(sticks))
