import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    keys = set(list(sys.stdin.readline().rstrip()))

    count = 0
    # BFS 시작점
    edges = []
    edge_doors = []
    # 가장자리. 빈곳.
    for y in range(h):
        for x in range(w):
            if (y == 0 or y == h - 1 or x == 0 or x == w - 1) and board[y][x] != '*':
                # 빈공간인 경우
                if board[y][x] == ".":
                    edges.append((y, x))
                # 문서인 경우
                elif board[y][x] == '$':
                    count += 1
                    edges.append((y, x))
                    board[y][x] = "."
                # 열쇠인 경우
                elif board[y][x].islower():
                    keys.add(board[y][x])
                    edges.append((y, x))
                    board[y][x] = "."
                # 문인 경우
                elif board[y][x].isupper():
                    # 키가 있는 경우
                    if board[y][x].lower() in keys:
                        edges.append((y, x))
                        board[y][x] = "."
                    # 키가 없는 경우. BFS 돌면서 열수있는지 판단해야한다.
                    else:
                        edge_doors.append((y, x))


    # 열쇠/문/문서에 대한 행동이 존재.
    actions = True
    while actions:
        actions = False

        # 진입점을 넣는다.
        visited = set(edges)
        Q = deque(edges)
        while Q:
            y, x = Q.popleft()

            # 주변을 탐색한다.
            for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                ny, nx = y + dy, x + dx
                if (ny, nx) in visited:
                    continue
                if not (0 <= ny < h and 0 < nx < w):
                    continue
                if board[ny][nx] == "*":
                    continue
                # 빈공간
                if board[ny][nx] == ".":
                    visited.add((ny, nx))
                    Q.append((ny, nx))
                # 대문자 -> 문을 여는 경우
                elif board[ny][nx].isupper() and board[ny][nx].lower() in keys:
                    visited.add((ny, nx))
                    Q.append((ny, nx))
                    board[ny][nx] = "."
                    actions = True
                # 소문자 -> 열쇠 획득
                elif board[ny][nx].islower():
                    keys.add(board[ny][nx])
                    visited.add((ny, nx))
                    Q.append((ny, nx))
                    board[ny][nx] = "."
                    actions = True
                # $ 문서 획득
                elif board[ny][nx] == '$':
                    visited.add((ny, nx))
                    Q.append((ny, nx))
                    board[ny][nx] = "."
                    actions = True
                    count += 1
            # 테두리 문을 열수 있는가?
            for y, x in edge_doors:
                if board[y][x].lower() in keys:
                    edges.append((y, x))
                    board[y][x] = "."
                    actions = True

    print(count)
