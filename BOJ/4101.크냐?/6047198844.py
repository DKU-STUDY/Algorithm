import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")
