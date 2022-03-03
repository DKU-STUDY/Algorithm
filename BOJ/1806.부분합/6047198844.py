import math
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

begin = 0
end = 0
part_sum = arr[begin]
part_len = math.inf
for begin in range(N):
    while end < N and part_sum < S:
        end += 1
        if end != N:
            part_sum += arr[end]
    if end == N:
        break
    part_len = min(part_len, end - begin + 1)
    part_sum -= arr[begin]

print(0) if part_len == math.inf else print(part_len)