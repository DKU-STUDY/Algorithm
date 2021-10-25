import sys

N = int(input())
ropes = list()
for _ in range(N):
    ropes.append(float(sys.stdin.readline()))

res = 0
for i in range(N):
    tmp = ropes[i]
    res = res if res > tmp else tmp
    for j in range(i + 1, N):
        tmp *= ropes[j]
        res = res if res > tmp else tmp

print(round(res, 3))
