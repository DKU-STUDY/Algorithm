import sys

sys.setrecursionlimit(10 ** 9)


# 가로/세로 크기, 현재 위치, 답 위치, 몇번째 방문인가.
def func(N, cy, cx, ty, tx, cnt):
    # 기저
    if N == 2:
        return cnt + 2 * (ty - cy) + (tx - cx)

    # 상
    if cy + N // 2 > ty:
        # 좌
        if cx + N // 2 > tx:
            return func(N // 2, cy, cx, ty, tx, cnt)
        # 우
        else:
            return func(N // 2, cy, cx + N // 2, ty, tx, cnt + (N // 2) * (N // 2))
    # 하
    else:
        # 좌
        if cx + N // 2 > tx:
            return func(N // 2, cy + N // 2, cx, ty, tx, cnt + 2 * (N // 2) * (N // 2))
        # 우
        else:
            return func(N // 2, cy + N // 2, cx + N // 2, ty, tx, cnt + 3 * (N // 2) * (N // 2))


N, r, c = map(int, sys.stdin.readline().split())
print(func(2 ** N, 0, 0, r, c, 0))
