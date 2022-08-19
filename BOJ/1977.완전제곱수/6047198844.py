import sys


def func(i):
    for j in range(1, i + 1):
        if i // j == j and i % j == 0:
            return True
    return False

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
res_sum = 0
res_min = sys.maxsize

for i in range(M,N + 1):
    if func(i):
        res_sum += i
        res_min = min(res_min, i)
if res_sum == 0:
    print(-1)
else:
    print(res_sum)
    print(res_min)
