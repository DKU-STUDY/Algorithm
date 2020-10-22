from sys import stdin


def compute(n):
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    return compute(n - 1) + compute(n - 2) + compute(n - 3)


def sol():
    n = int(stdin.readline())
    print(compute(n))


T = int(stdin.readline())

for _ in range(T):
    sol()
