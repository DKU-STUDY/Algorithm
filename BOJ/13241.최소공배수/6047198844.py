import sys

a, b = map(int ,sys.stdin.readline().split())

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
print(a * b // gcf(a, b))