# memo[마지막수][방문]
'''
memo[0][0000000001] = 0
memo[1][0000000010] = 1
...
...
memo[9][1000000000] = 1
'''

N = int(input())
memo = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)]
for num in range(1, 9 + 1):
    memo[1][num][1 << num] = 1

# 길이가 2인 경우부터
for S in range(2, N + 1):
    # 끝이 0인 경우. 끝자리가 1인 경우를 모두 합친다.
    for k in range(1 << 10):
        memo[S][0][k | (1 << 0)] += memo[S-1][1][k] % 1000000000

    # 끝이 1~8인 경우
    for num in range(1, 8 + 1):
        for k in range((1 << 10)):
            memo[S][num][k | (1 << num)] += (memo[S-1][num - 1][k] % 1000000000 + memo[S-1][num + 1][k] % 1000000000) % 1000000000

    # 끝이 9인 경우. 끝자리가 8인 경우를 모두 합친다.
    for k in range((1 << 10)):
        memo[S][9][k | (1 << 9)] += memo[S-1][8][k] % 1000000000

res = 0
for i in range(9 + 1):
    res += memo[N][i][(1 << 10) - 1] % 1000000000
print(res % 1000000000)
