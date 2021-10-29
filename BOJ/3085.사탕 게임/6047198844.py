from itertools import permutations

N = int(input())

board = list()
for _ in range(N):
    board.append(list(input()))

cord = range(0, N)
res = 0


def bom(board):
    # 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
    cnt = 0
    for row in board:
        for color in ('C', 'P', 'Z', 'Y'):
            tmp = 0
            for element in row:
                if element == color:
                    tmp += 1
                else:
                    cnt = max(cnt, tmp)
                    tmp = 0

            cnt = max(cnt, tmp)

    for column in zip(board):
        for color in ('C', 'P', 'Z', 'Y'):
            tmp = 0
            for element in column:
                if element == color:
                    tmp += 1
                else:
                    cnt = max(cnt, tmp)
                    tmp = 0

            cnt = max(cnt, tmp)

    return cnt


for ay, ax in permutations(cord, 2):
    for by, bx in permutations(cord, 2):
        if board[ay][ax] != board[by][bx]:
            board[ay][ax], board[by][bx] = board[by][bx], board[ay][ax]
            res = max(res, bom(board))
            board[ay][ax], board[by][bx] = board[by][bx], board[ay][ax]
print(res)
