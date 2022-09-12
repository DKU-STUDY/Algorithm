import sys

G = int(sys.stdin.readline())
weight = [x for x in range(1, 100001)]
N, M = 100000, 100000
left, right = 0, 0  # 투 포인터
arr = set()
# i = x+y
# j = x-y
ans = []
while left < N and right < M:
    tmp = (weight[left] + weight[right]) * (weight[left] - weight[right])
    if tmp == G:
        ans.append(weight[left])
    if tmp < G:
        left += 1
    else:
        right += 1
if not ans:
    print(-1)
    exit()
for y in ans:
    print(y)
