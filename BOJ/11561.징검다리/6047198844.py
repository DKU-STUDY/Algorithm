import sys

T = int(sys.stdin.readline())


def sol(N):
    # N에 도달할수있는가.
    # lower_bound를 찾는다.
    l = 1
    r = 10 ** 10
    while l < r:
        mid = (l + r) // 2
        if (mid ** 2 + mid) // 2 <= N:
            l = mid + 1
        else:
            r = mid
    return r - 1


for _ in range(T):
    print(sol(int(sys.stdin.readline())))
