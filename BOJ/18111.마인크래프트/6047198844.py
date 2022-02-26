# 문제
# lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다.
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
# 1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.
# ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
# 단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다.
# 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.
#
# 입력
# 첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
#
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
import math
import sys

N, M, B = map(int, sys.stdin.readline().split())
lands = []
for _ in range(N):
    for i in map(int, sys.stdin.readline().split()):
        lands.append(i)
lands.sort(reverse=True)
max_height, min_height = lands[0], lands[-1]

res_time = math.inf
res_height = max_height

# 요구 높이.
for height in range(max_height, min_height - 1, -1):
    inventory = B
    count = 0
    for land in lands:
        # 요구 높이 보다 크다면.
        if land > height:
            # 차이
            dif = land - height
            # 인벤토리에 추가한다.
            inventory += dif
            # 차이만큼 요금을 부과한다.
            count += dif * 2
        elif land < height:
            # 차이
            dif = height - land
            if inventory >= dif:
                # 차이만큼 인벤토리에서 뽑는다.
                inventory -= dif
                # 차이만큼 요금을 부과한다.
                count += dif
            # 못뽑으면 탈출한다.
            else:
                break
    else:
        if res_time > count:
            res_time = count
            res_height = height

print(res_time, res_height, sep=' ')