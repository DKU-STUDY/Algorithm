import sys

res = 0
while True:
    N = int(sys.stdin.readline())
    if N == -1:
        print(res)
        exit()
    res += N