import collections
import copy

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
#이 보드에 zero끼리 섬을 나누고 섬에 해당하는 0의 개수와 섬의 번호를 저장한다.
zero_board = [[(0, -1) for _ in range(M)] for _ in range(N)]


#zero_board를 만든다.
#zero_board란 zero끼리 이루는 섬의 zero개수이다.
def zero_bfs(i, j, group):
    #자기 자신을 포함한다.
    zero_cnt = 1
    Q = collections.deque()
    Q.append((i,j))
    visited = set()
    visited.add((i,j))

    while Q:
        y, x = Q.popleft()
        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0 and (ny, nx) not in visited:
                    zero_cnt += 1
                    Q.append((ny, nx))
                    visited.add((ny, nx))
    for y, x in visited:
        zero_board[y][x] = (zero_cnt, group)

group = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == 0 and zero_board[y][x][0] == 0:
            zero_bfs(y, x, group)
            group += 1

#group 주의.
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == 1:
            visited = set()
            for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0 and zero_board[ny][nx][1] not in visited:
                    board[y][x] += zero_board[ny][nx][0]
                    visited.add(zero_board[ny][nx][1])
            board[y][x] %= 10

for row in board:
    print(*row, sep='')