import math
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    hired = [0] * (N+1)
    for _ in range(N):
        rank_i, rank_j = map(int, sys.stdin.readline().split())
        hired[rank_i] =  rank_j

        m = math.inf
        cnt = 0
        for i in range(1, N+1):
            if m > hired[i]:
                m = hired[i]
                cnt += 1
    print(cnt)