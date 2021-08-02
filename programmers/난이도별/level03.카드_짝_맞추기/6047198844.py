import collections
import sys
from itertools import permutations


def solution(board, r, c):
    def ctrl(y, x, dy, dx):
        while 0 <= y < 4 and 0 <= x < 4:
            y += dy
            x += dx
            if (y, x) in SET:
                return (y, x)
        if 0 <= y < 4:
            return (y, x-dx)
        else:
            return (y-dy, x)

    # dept에서 dest로 갈때 최소 비용을 반납한다.
    def dept_to_dest(A, B):
        # A에서 B로 이동하는 최소비용
        direction = set()
        Q = [A]
        cmd = 0
        while True:
            for _ in range(len(Q)):
                y, x = Q.pop(0)
                if (y, x) == B:
                    return cmd
                # 좌우상하
                # 컨트롤 좌우상하
                for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < 4 and 0 <= nx < 4 and not (ny, nx) in direction:
                        direction.add((ny, nx))
                        Q.append((ny, nx))

                    cny, cnx = ctrl(y, x, dy, dx)
                    if not (cny, cnx) in direction:
                        direction.add((cny, cnx))
                        Q.append((cny, cnx))
            cmd += 1

    def short_path(cursor, dist):
        if not dist:
            return 0
        # cursor -> A
        # A -> B
        A, B = dist[0]
        # cursor -> A -> B
        i = dept_to_dest(cursor, A) + 1 + dept_to_dest(A, B) + 1
        # cursor -> B -> A
        j = dept_to_dest(cursor, B) + 1 + dept_to_dest(B, A) + 1

        SET.remove(A)
        SET.remove(B)
        i += short_path(B, dist[1:])
        j += short_path(A, dist[1:])
        SET.add(A)
        SET.add(B)

        return min(i, j)
    # a에서 b로 갈때 드는 최소비용반환.
    # 6!
    answer = sys.maxsize

    cards = collections.defaultdict(list)

    for y in range(0, 4):
        for x in range(0, 4):
            if board[y][x] != 0:
                cards[board[y][x]].append((y, x))

    SET = set()
    for card1, card2 in cards.values():
        SET.add(card1)
        SET.add(card2)

    for p in permutations(cards.values()):
        answer = min(answer, short_path((r, c), p))

    return answer