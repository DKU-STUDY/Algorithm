import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    memo1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    memo2 = list(map(int, sys.stdin.readline().split()))
    for integer in memo2:
        print(int(integer in memo1))