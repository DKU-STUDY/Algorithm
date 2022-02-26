import sys

# M 목표 바이트.
N, M = map(int, sys.stdin.readline().split())
# 메모리
m = [0] + list(map(int, sys.stdin.readline().split()))
# 비용
c = [0] + list(map(int, sys.stdin.readline().split()))

# memo 의 정의부터 세운다.
# memo[i][cost] = cost의 비용을 지불한다고 가정했을때 i 번째까지의 어플까지 확보할수있는 최대 메모리값.
# j 의 범위는 ? 비용의 합. 즉 최대 10000
total_cost = sum(c)
res = total_cost

memo = [[0 for _ in range(total_cost + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for cost in range(total_cost + 1):
        # 현재 어플리케이션 i를 비활성화시 메모리를 얻는다.
        # 비활성화하게 되면 cost 를 주어야한다.
        # 현재 메모리값을 확보하려면 이전의 최적값을 알아야한다. 직전의 최적값에 현재 어플리케이션을 비활성화 해보자.
        # 활성화는 메모리를 오히려 잡아먹으니 하지 않는다.
        # 이전의 최적값은 memo[직전까지 확보한값][현재 지불하고자하는 비용 - 현재 어플리케이션의 비용] + 현재 어플리케이션으로 확보가능한 메모리
        # 비용을 지불못하면 스킵.
        if cost < c[i]:
            memo[i][cost] = memo[i - 1][cost]
        # 비용을 지불, 비활성화 하고 메모리를 받는다.
        else:
            memo[i][cost] = max(memo[i - 1][cost], memo[i - 1][cost - c[i]] + m[i])

        # 현재 확보한 메모리가 요구하는 메모리보다 크면 답을 교체한다.
        if M <= memo[i][cost]:
            res = min(res, cost)
print(res)