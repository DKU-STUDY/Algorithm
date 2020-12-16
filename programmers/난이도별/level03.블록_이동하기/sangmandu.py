'''
https://programmers.co.kr/learn/courses/30/lessons/60063
블록 이동하기
stack, save를 이용한 BFS
visited를 두 좌표에 적용해서 동시에 방문했을 경우 reject
같은 좌표축에 있을 경우는 회전이 불가
'''

from collections import deque


def solution(board):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    size = len(board)
    visited = set()
    stack = deque()
    stack.append((0, 0, 0, 1, 0))
    save = deque()
    visited.add(((0, 0), (0, 1)))

    while True:
        if not stack:
            stack, save = save, stack
        lx, ly, rx, ry, dist = stack.popleft()
        if rx == ry == size - 1 or lx == ly == size - 1:
            return dist

        for x, y in move:
            nlx = lx + x
            nly = ly + y
            nrx = rx + x
            nry = ry + y

            if ((nlx, nly), (nrx, nry)) in visited:
                continue
            if nlx < 0 or nlx >= size or nly < 0 or nly >= size:
                continue
            if nrx < 0 or nrx >= size or nry < 0 or nry >= size:
                continue
            if board[nlx][nly] == 1 or board[nrx][nry] == 1:
                continue

            save.append((nlx, nly, nrx, nry, dist + 1))
            visited.add(((lx, ly), (rx, ry)))
            visited.add(((rx, ry), (lx, ly)))
            if (x != 0 and lx == rx) or (y != 0 and ly == ry):
                if ((lx, ly), (nlx, nly)) not in visited:
                    save.append((lx, ly, nlx, nly, dist + 1))
                    visited.add(((lx, ly), (nlx, nly)))
                    visited.add(((nlx, nly), (lx, ly)))
                if ((nrx, nry), (rx, ry)) not in visited:
                    save.append((nrx, nry, rx, ry, dist + 1))
                    visited.add(((nrx, nry), (rx, ry)))
                    visited.add(((rx, ry), (nrx, nry)))

'''
시간초과가 발생해서 2주는 걸린 문제.
stack에 추가할 때 visited를 바로 갱신해야 중복 케이스가 생기지 않는 것을 알게 되었다.
'''