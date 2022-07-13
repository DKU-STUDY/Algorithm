import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = set()


def func(y, x):
    if y >= N or x >= N:
        return False
    if (y, x) in visited:
        return False
    if y == N - 1 and x == N - 1:
        return True

    visited.add((y, x))
    if func(y + board[y][x], x):
        return True
    if func(y, x + board[y][x]):
        return True

if func(0, 0):
    print('HaruHaru')
else:
    print('Hing')
