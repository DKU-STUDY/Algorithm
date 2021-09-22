T = int(input())
L = list()
for _ in range(T):
    L.append(int(input()))
N = sorted(L)[-1]

# 0 : 짝수 / 1 : 홀수
memo = [[0, 0] for _ in range(N + 1)]
# 1 : 1
memo[1][1] = 1
# 2 : 1+1, 2
memo[2][0] = 1
memo[2][1] = 1
# 3 : 1+1+1, 1+2, 2+1, 3
memo[3][0] = 2
memo[3][1] = 2

for i in range(4, N + 1):
    # 1더하기 / 2더하기 / 3더하기
    memo[i][0] = (memo[i - 1][1] % 1000000009 + memo[i - 2][1] % 1000000009 + memo[i - 3][1] % 1000000009) % 1000000009
    memo[i][1] = (memo[i - 1][0] % 1000000009 + memo[i - 2][0] % 1000000009 + memo[i - 3][0] % 1000000009) % 1000000009

for i in L:
    print(memo[i][1], memo[i][0])
