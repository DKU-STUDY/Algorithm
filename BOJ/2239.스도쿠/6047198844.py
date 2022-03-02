# 개요
# 스도쿠 풀기
import sys

board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
# area (y // 3) * 3 + x // 3
area = [set() for _ in range(9)]
row = [set() for _ in range(9)]
column = [set() for _ in range(9)]

# 초기화
for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
            row[y].add(board[y][x])
            column[x].add(board[y][x])
            area[(y // 3) * 3 + x // 3].add(board[y][x])


# 현재 위치가 y, x 때 경우의 수를 다 놓는 함수.
def func(y, x):
    # 예외: x가 범위를 벗어 났을때. y로 옮겨서 탐색 지속
    if x == 9:
        return func(y + 1, 0)

    # base case: y가 범위를 벗어 난 경우. 프로그램 종료.
    if y == 9:
        for line in board:
            print(''.join(map(str, line)))
        exit()

    # 예외2: 이미 배치된 경우. 탐색 계속
    if board[y][x] != 0:
        return func(y, x + 1)

    # backtracking
    for i in range(1, 9 + 1):
        # 예외3 : 같은 행/열/구역에 이미 배치된 경우. 탐색 종료
        if i in row[y] or i in column[x] or i in area[(y // 3) * 3 + x // 3]:
            continue
        board[y][x] = i
        row[y].add(i)
        column[x].add(i)
        area[(y // 3) * 3 + x // 3].add(i)

        func(y, x + 1)

        area[(y // 3) * 3 + x // 3].remove(i)
        column[x].remove(i)
        row[y].remove(i)
        board[y][x] = 0


func(0, 0)
