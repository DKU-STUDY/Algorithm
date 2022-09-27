import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(sum(map(int,sys.stdin.readline().split())))