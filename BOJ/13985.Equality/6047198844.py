import sys

input = sys.stdin.readline().split()
plus = int(input[0]) + int(input[2])
result = int(input[4])

if plus == result:
    print("YES")
else:
    print("NO")