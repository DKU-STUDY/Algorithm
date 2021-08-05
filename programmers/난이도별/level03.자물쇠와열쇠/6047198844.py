def solution(key, lock):
    def key_rotate(rkey):
        return list(zip(*rkey[::-1]))

    def is_valid(board):
        for y in range(M, M + N):
            for x in range(M, M + N):
                if board[y][x] != 1:
                    return False
        return True

    def unlock(yy, xx, board, flag):
        for y in range(yy, yy + M):
            for x in range(xx, xx + M):
                board[y][x] += (key[y - yy][x - xx] * flag)

    # lock를 NXN칸의 중앙으로 놓자.
    M = len(key)
    N = len(lock)
    # 흰 판을 준비한다.
    board = [[0 for _ in range(N + 2 * M)] for _ in range(N + 2 * M)]

    # 흰 판에 튀어나온 부분을 입힌다.
    for y in range(M, M + N):
        for x in range(M, M + N):
            board[y][x] = lock[y - M][x - M]

    # print_board(board)
    # key를 4방향으로 90도씩 돌려가며 비교한다.
    for _ in range(4):
        key = key_rotate(key)
        for y in range(0, N + M):
            for x in range(0, N + M):
                unlock(y, x, board, +1)
                if is_valid(board):
                    return True
                unlock(y, x, board, -1)
    return False