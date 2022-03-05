import sys
from copy import deepcopy


def move():
    global board
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            while board[y][x]:
                shark_idx = board[y][x].pop()
                ny, nx, nspeed, ndirection, nsize = sharks[shark_idx]
                # 위 , 아래 , 오른쪽 , 왼쪽
                # 거리축소
                if ndirection == 1 or ndirection == 2:
                    ndistance = nspeed % (2 * (R - 1))
                else:
                    ndistance = nspeed % (2 * (C - 1))

                # 거리만큼 움직인다.
                cnt = 0
                while cnt < ndistance:
                    # 위
                    if ndirection == 1:
                        # 방
                        if ny == 0:
                            ndirection = 2
                            continue
                        ny -= 1
                    # 아래
                    elif ndirection == 2:
                        # 방
                        if ny == R - 1:
                            ndirection = 1
                            continue
                        ny += 1
                    # 오른쪽
                    elif ndirection == 3:
                        # 방
                        if nx == C - 1:
                            ndirection = 4
                            continue
                        nx += 1
                    # 왼쪽
                    elif ndirection == 4:
                        # 방
                        if nx == 0:
                            ndirection = 3
                            continue
                        nx -= 1
                    # 움직인다.
                    cnt += 1

                sharks[shark_idx] = (ny, nx, nspeed, ndirection, nsize)
                new_board[ny][nx].append(shark_idx)

    # 모두 이동한 후에 board 에 반영한다.
    board = deepcopy(new_board)


def remove_shark():
    for y in range(R):
        for x in range(C):
            if len(board[y][x]) > 1:
                max_shark_idx = max(board[y][x], key=lambda idx: sharks[idx][4])
                board[y][x] = [max_shark_idx]


R, C, M = map(int, sys.stdin.readline().split())

sharks = []
board = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    y, x, speed, direction, size = map(int, sys.stdin.readline().split())
    sharks.append((y - 1, x - 1, speed, direction, size))
    board[y - 1][x - 1].append(i)

fisher = -1
res = 0

while True:
    # 낚시왕이 이동한다
    fisher += 1
    if fisher == C:
        print(res)
        exit()

    # 낚시왕 인덱스를 x 로 가지는 상어중에 가장 y 가 작은 상어 삭제.
    for ny in range(R):
        # shark 가 아닌경우.
        if len(board[ny][fisher]) == 0:
            continue
        # shark 인 경우
        # 잡는다.
        shark_idx = board[ny][fisher].pop(0)
        res += sharks[shark_idx][4]
        break

    # 상어를 이동한다.
    move()

    # 겹치는 상어 제거한다.
    remove_shark()
