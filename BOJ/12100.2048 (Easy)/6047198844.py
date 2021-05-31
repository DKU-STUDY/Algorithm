# 4진수로 변경한다. 5번의 행동에 대해 반환한다.
import copy


def convert_binary_quaternary(binary_command):
    quaternary_command = []
    for _ in range(5):
        quaternary_command.append(binary_command & 3)
        binary_command = binary_command >> 2
    return quaternary_command

# 명령이 주어진대로(상하좌우) 움직인다.
# 명령, board
# 움직인후 최대값을 반환한다.
def move_up(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            #현재값이 0이 아니라면
            if board[y][x] != 0:
                #이전값이 범위에 있고 0이라면
                ny = y
                #이동 가능한 위치를 탐색한다.
                while ny - 1 >= 0 and board[ny - 1][x] == 0:
                    ny -= 1
                #이동이 이루어 진다면
                if ny != y:
                    board[ny][x] = board[y][x]
                    board[y][x] = 0
    return

def move_down(board):
    for y in range(len(board)-1,-1,-1):
        for x in range(len(board[0])):
            #현재값이 0이 아니라면
            if board[y][x] != 0:
                #이전값이 범위에 있고 0이라면
                ny = y
                #이동 가능한 위치를 탐색한다.
                while ny + 1 < N and board[ny + 1][x] == 0:
                    ny += 1
                #이동이 이루어 진다면
                if ny != y:
                    board[ny][x] = board[y][x]
                    board[y][x] = 0
    return

def move_left(board):
    for x in range(len(board[0])):
        for y in range(len(board)):
            #현재값이 0이 아니라면
            if board[y][x] != 0:
                #이전값이 범위에 있고 0이라면
                nx = x
                #이동 가능한 위치를 탐색한다.
                while nx - 1 >= 0 and board[y][nx - 1] == 0:
                    nx -= 1
                #이동이 이루어 진다면
                if nx != x:
                    board[y][nx] = board[y][x]
                    board[y][x] = 0
    return

def move_right(board):
    for x in range(len(board[0]) - 1, -1, -1):
        for y in range(len(board)):
            # 현재값이 0이 아니라면
            if board[y][x] != 0:
                # 이전값이 범위에 있고 0이라면
                nx = x
                # 이동 가능한 위치를 탐색한다.
                while nx + 1 < N and board[y][nx + 1] == 0:
                    nx += 1
                # 이동이 이루어 진다면
                if nx != x:
                    board[y][nx] = board[y][x]
                    board[y][x] = 0
    return

def add_up(board):
    for y in range(1, len(board)):
        for x in range(len(board[0])):
            if board[y][x] != 0 and board[y-1][x] == board[y][x]:
                board[y-1][x] += board[y][x]
                board[y][x] = 0

def add_down(board):
    for y in range(len(board) - 2, -1, -1):
        for x in range(len(board[0])):
            if board[y][x] != 0 and board[y + 1][x] == board[y][x]:
                board[y + 1][x] += board[y][x]
                board[y][x] = 0

def add_left(board):
    for x in range(1, len(board[0])):
        for y in range(len(board)):
            if board[y][x] != 0 and board[y][x - 1] == board[y][x]:
                board[y][x - 1] += board[y][x]
                board[y][x] = 0

def add_right(board):
    for x in range(len(board[0]) - 2, -1, -1):
        for y in range(len(board)):
            if board[y][x] != 0 and board[y][x + 1] == board[y][x]:
                board[y][x + 1] += board[y][x]
                board[y][x] = 0


def move_board(commands, board):
    for command in commands:
        # 상
        # 한칸씩 올려야 한다.
        if command == 0:
            pass
            #숫자를 모두 올린다. 덧샘 없이.
            move_up(board)
            add_up(board)
            move_up(board)

        # 하
        # 한칸씩 내려야 한다.
        elif command == 1:
            #숫자를 모두 내린다. 덧샘 없이
            move_down(board)
            add_down(board)
            move_down(board)

        # 좌
        elif command == 2:
            move_left(board)
            add_left(board)
            move_left(board)

        # 우
        else:
            move_right(board)
            add_right(board)
            move_right(board)

    return max(map(max, board))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

#모든 경우의 수에 대해 생각한다.
#4^5 ==> 2^10
res = -1
for binary_command in range(1 << 10):
    quaternary_command = convert_binary_quaternary(binary_command)
    res = max(res, move_board(quaternary_command, copy.deepcopy(board)))

print(res)

# 2차원배열에서 max값을 구하는 법
# https://devbull.xyz/python-2caweon-baeyeolyi-coedaegabs-coesogabs-cajgi/
