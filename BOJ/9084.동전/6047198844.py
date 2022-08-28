import sys

T = int(sys.stdin.readline())


# i: 현재 코인 인덱스
# coins: 코인
# K: 목표치
def dp(K, coins):
    memo = [0] * (K + 1)
    # memo[K] = K 원을 만들 수 있는 경우의 수
    # 0 원을 만드는 경우의 수는 하나이다.
    memo[0] = 1
    for coin in coins:
        for i in range(K+1):
            if i - coin >= 0:
                memo[i] = memo[i] + memo[i-coin]
    return memo[K]


for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    K = int(sys.stdin.readline())
    print(dp(K, coins))