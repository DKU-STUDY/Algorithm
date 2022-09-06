import sys

N = int(sys.stdin.readline())
for _ in range(N):
    res = 0
    car_price = int(sys.stdin.readline())
    res += car_price
    option_N = int(sys.stdin.readline())
    for _ in range(option_N):
        quantity, option_price = map(int, sys.stdin.readline().split())
        res += (quantity * option_price)
    print(res)