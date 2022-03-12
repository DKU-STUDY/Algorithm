import math

commands = list(map(int, input().split()))
memo = [[[math.inf for _ in range(5)] for _ in range(5)] for _ in range(len(commands))]
memo[0] = [[0 for _ in range(5)] for _ in range(5)]

for idx, command in enumerate(commands[:-1]):
    # 초기 상태라면 , 항상 비용이 2가 든다.
    if idx == 0:
        memo[idx + 1][0][command] = 2
        memo[idx + 1][command][0] = 2
        continue

    # 왼발이 움직이는 경우.
    # 이전 오른발의 초기상태. 오른발은 고정이다.
    for fix in range(4 + 1):
        if fix == command:
            continue
        # 이전 왼발의 상태. 왼발은 움직인다.
        for move in range(4 + 1):
            if move == command:
                memo[idx + 1][command][fix] = min(memo[idx + 1][command][fix], memo[idx][move][fix] + 1)
                memo[idx + 1][fix][command] = min(memo[idx + 1][fix][command], memo[idx][fix][move] + 1)
            elif move == 0:
                memo[idx + 1][command][fix] = min(memo[idx + 1][command][fix], memo[idx][move][fix] + 2)
                memo[idx + 1][fix][command] = min(memo[idx + 1][fix][command], memo[idx][fix][move] + 2)
            elif ((move == 1 or move == 3) and (command == 2 or command == 4)) or (
                    (move == 2 or move == 4) and (command == 1 or command == 3)):
                memo[idx + 1][command][fix] = min(memo[idx + 1][command][fix], memo[idx][move][fix] + 3)
                memo[idx + 1][fix][command] = min(memo[idx + 1][fix][command], memo[idx][fix][move] + 3)
            else:
                memo[idx + 1][command][fix] = min(memo[idx + 1][command][fix], memo[idx][move][fix] + 4)
                memo[idx + 1][fix][command] = min(memo[idx + 1][fix][command], memo[idx][fix][move] + 4)

res = math.inf
for r in memo[-1]:
    res = min(res, min(r))
print(res)
