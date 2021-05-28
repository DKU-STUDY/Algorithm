# 현재 시점을 기점으로 만들수있는 최대 이익을 반환한다.
def dfs(start_day):
    # 퇴사했으므로 일을 시작할 수 없다.
    if start_day == N + 1:
        return 0

    global memo
    # 현재 시점이 저장되어 있는가?
    if memo[start_day] != -1:
        return memo[start_day]

    # 현재 시점의 누적금액. 아직 일을 진행하지 않은 상태이다.
    res = 0

    # 현재시점을 진행하는데 드는 비용 = (시간비용, 돈비용)
    time_cost, money_cost = bill[start_day]

    # 기간내에 일을 끝내고 난 후의 범위
    for day in range(time_cost + start_day, N + 2):
        res = max(res, money_cost + dfs(day))

    memo[start_day] = res
    return memo[start_day]


N = int(input())

# (시간 , 비용)
bill = [(1, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
memo = [-1] * (N + 1)
print(dfs(0))
