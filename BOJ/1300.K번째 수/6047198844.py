import sys


def rank(m):
    mn, mx = 0, 0
    for i in range(1, N + 1):
        mx = mx + min(m // i, N)
        mn = mn + min(m // i, N)
        if m % i == 0 and m <= N*i:
            mn -= 1
    return mn, mx


N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

begin, end = 1, 10**10

while begin < end:
    mid = (begin + end) // 2

    mn, mx = rank(mid)
    # 구한값이 실제보다 작다. -> 높히자
    if mn < k <= mx:
        begin = mid
        break
    elif mx < k:
        begin = mid + 1
    else:
        end = mid - 1
print(begin)
# 1*1 2*1 3*1
# 1*2 2*2 3*2
# 1*3 2*3 3*3

#  1 2 3 4 5 6 7 8 9
#  1 2 2 3 3 4 6 6 9

# 1 ~ 7
# 5 ~ 7
