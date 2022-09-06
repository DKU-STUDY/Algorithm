import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
numerator = A * D + C * B
denominator = B * D
while True:
    div = gcd(numerator, denominator)
    if div == 1:
        print(numerator, denominator)
        exit()
    numerator //= div
    denominator //= div
