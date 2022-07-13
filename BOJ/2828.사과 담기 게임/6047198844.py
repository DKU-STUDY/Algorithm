import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
positions = [int(sys.stdin.readline()) for _ in range(J)]

left = 1
right = M

distance = 0
for position in positions:
    while position < left:
        left -= 1
        right -= 1
        distance += 1

    while position > right:
        left += 1
        right += 1
        distance += 1

print(distance)