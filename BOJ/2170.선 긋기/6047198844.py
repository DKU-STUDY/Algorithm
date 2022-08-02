import math
import sys

N = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort()

res = 0
left = -1000000001
right = -1000000001

for line in lines:
    begin, end = line
    # 이전과 이을수없는 경우.
    if right < begin:
        # 이전의 거리를 계산한다.
        res += right - left
        # 새로운 선으로 교체한다.
        left, right = begin, end
    # 이전과 이을수있는 경우
    else:
        right = max(right, end)

print(res + right - left)