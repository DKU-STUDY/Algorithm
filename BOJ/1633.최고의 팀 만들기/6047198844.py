# 완전 탐색.
# 경우의 수
# 선택하는 경우
#   흑 팀을 선택하는 경우
#   백 팀을 선택하는 경우
# 선택하지 않은 경우
import sys

# 입력

lines = sys.stdin.readlines()
members = [tuple(map(int, line.split())) for line in lines]
memo = [[[0 for _ in range(15 + 1)] for _ in range(15 + 1)] for _ in range(len(members))]


# 독립적이다.
def dfs(idx: int, white, black):
    # base case 1 : idx 이상이 존재하지 않는 경우
    if idx == len(members):
        return 0
    # base case 2 : white, black 선수단이 꽉찬 경우
    if white == 0 and black == 0:
        return 0
    # base case 3 : 탐색이 완료된 케이스의 경우
    if memo[idx][white][black] != 0:
        return memo[idx][white][black]

    # 선택하는 경우
    #   백 팀을 선택하는 경우
    if white > 0:
        memo[idx][white][black] = max(memo[idx][white][black], dfs(idx + 1, white - 1, black) + members[idx][0])
    #   흑 팀을 선택하는 경우
    if black > 0:
        memo[idx][white][black] = max(memo[idx][white][black], dfs(idx + 1, white, black - 1) + members[idx][1])
    # 선택하지 않은 경우
    memo[idx][white][black] = max(memo[idx][white][black], dfs(idx + 1, white, black))
    return memo[idx][white][black]


# idx 번째 이상 선택이 가질수있는 높은 플레이 능력치의 합
# idx, 남은 흑팀 수, 남은 백팀수
print(dfs(0, 15, 15))
