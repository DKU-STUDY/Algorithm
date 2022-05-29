import sys


def is_prime(i):
    if i < 2:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def dfs(i, cnt):
    if cnt == N:
        print(i)
        return

    for p in range(1, 10, 2):
        if is_prime(i * 10 + p):
            dfs(i * 10 + p, cnt + 1)


N = int(sys.stdin.readline())
for i in 2,3,5,7:
    dfs(i, 1)