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
    for right in range(4 + 1):
        if right == command:
            continue
        # 이전 왼발의 상태. 왼발은 움직인다.
        for left in range(4 + 1):
            if left == command:
                memo[idx + 1][command][right] = min(memo[idx + 1][command][right], memo[idx][left][right] + 1)
            elif left == 0:
                memo[idx + 1][command][right] = min(memo[idx + 1][command][right], memo[idx][left][right] + 2)
            elif ((left == 1 or left == 3) and (command == 2 or command == 4)) or (
                    (left == 2 or left == 4) and (command == 1 or command == 3)):
                memo[idx + 1][command][right] = min(memo[idx + 1][command][right], memo[idx][left][right] + 3)
            else:
                memo[idx + 1][command][right] = min(memo[idx + 1][command][right], memo[idx][left][right] + 4)

    # 오른발이 움직이는 경우.
    # 이전 왼발의 초기상태. 왼발은 고정이다.
    for left in range(4 + 1):
        if left == command:
            continue
        # 이전 오른발의 상태. 오른발은 움직인다.
        for right in range(4 + 1):
            # right -> command
            if right == command:
                memo[idx + 1][left][command] = min(memo[idx + 1][left][command], memo[idx][left][right] + 1)
            elif right == 0:
                memo[idx + 1][left][command] = min(memo[idx + 1][left][command], memo[idx][left][right] + 2)
            elif ((right == 1 or right == 3) and (command == 2 or command == 4)) or (
                    (right == 2 or right == 4) and (command == 1 or command == 3)):
                memo[idx + 1][left][command] = min(memo[idx + 1][left][command], memo[idx][left][right] + 3)
            else:
                memo[idx + 1][left][command] = min(memo[idx + 1][left][command], memo[idx][left][right] + 4)

res = math.inf
for r in memo[-1]:
    res = min(res, min(r))
print(res)