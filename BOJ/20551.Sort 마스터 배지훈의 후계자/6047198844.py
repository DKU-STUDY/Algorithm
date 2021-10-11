# 1 <= N <= 2*10^5
# 1 <= M <= 2-10^5
import sys

N, M = map(int, input().split())
A = list()
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()

for _ in range(M):
    question = int(sys.stdin.readline())
    begin = 0
    end = N
    while begin < end:
        mid = (begin + end) // 2
        if A[mid] >= question:
            end = mid
        else:
            begin = mid + 1
    if 0 <= begin < N and A[begin] == question:
        print(begin)
    else:
        print(-1)
