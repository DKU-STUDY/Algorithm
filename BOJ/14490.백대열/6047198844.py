import sys


def func(a, b):
    if b == 0:
        return a
    return func(b, a % b)
a, b = map(int, sys.stdin.readline().split(':'))
gcf = func(a, b)
print(f'{a//gcf}:{b//gcf}')