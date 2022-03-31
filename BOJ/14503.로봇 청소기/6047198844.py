# 문제
# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.
# 로봇 청소기가 있는 장소는 N×M 크기의 정사각형이다.
# 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다.
# 로봇 청소기는 다음과 같이 작동한다.
#
# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
#
# 입력
# 첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)
# 둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
# 셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
# 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.
#
# 출력
# 로봇 청소기가 청소하는 칸의 개수를 출력한다.
import sys

# 행 / 열
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
clear = set()
while True:
    # 현재 위치를 청소한다.
    clear.add((r, c))

    # 4 방향 탐색
    for _ in range(4):
        # 상
        if d == 0:
            # 좌로 회전
            d = 3
            # 벽 / 청소한 경우.
            if board[r][c - 1] == 1 or (r, c - 1) in clear:
                continue
            else:
                c -= 1
                break
        # 우
        elif d == 1:
            # 상으로 회전
            d = 0
            # 벽 / 청소한 경우.
            if board[r - 1][c] == 1 or (r - 1, c) in clear:
                continue
            else:
                r -= 1
                break
        # 하
        elif d == 2:
            # 우로 회전
            d = 1
            # 벽 / 청소한 경우.
            if board[r][c + 1] == 1 or (r, c + 1) in clear:
                continue
            else:
                c += 1
                break
        # 좌
        else:
            # 하로 회전
            d = 2
            # 벽 / 청소한 경우.
            if board[r + 1][c] == 1 or (r + 1, c) in clear:
                continue
            else:
                r += 1
                break
    # 네 방향 모두 청소가 되어있는 경우
    else:
        # 상
        if d == 0:
            # 벽이 아님
            if board[r + 1][c] != 1:
                r += 1
            else:
                break
        # 우
        elif d == 1:
            # 벽이 아님
            if board[r][c - 1] != 1:
                c -= 1
            else:
                break
        # 하
        elif d == 2:
            # 벽이 아님
            if board[r - 1][c] != 1:
                r -= 1
            else:
                break

        # 좌
        else:
            # 벽이 아님
            if board[r][c + 1] != 1:
                c += 1
            else:
                break

print(len(clear))













