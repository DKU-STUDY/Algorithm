import math

N = int(input())
memo = [math.inf for _ in range(N+1)]
memo[0] = -1

# 경로 생성
for x in range(1, N + 1):
    # 모두 알아야하기때문에 if 로 엮는다.
    if x % 3 == 0:
        memo[x] = min(memo[x], memo[x//3] + 1)
    if x % 2 == 0:
        memo[x] = min(memo[x], memo[x//2] + 1)
    memo[x] = min(memo[x], memo[x-1] + 1)

print(memo[N])
# 경로 추적
x = N
routes = [N]
while x != 1:
    # 아무거나 해도 되기때문에 if else 로 엮는다.
    if x % 3 == 0 and memo[x] == memo[x//3] + 1:
        x //= 3
    elif x % 2 == 0 and memo[x] == memo[x//2] + 1:
        x //= 2
    else:
        x -= 1
    routes.append(x)

for route in routes:
    print(route, end=' ')