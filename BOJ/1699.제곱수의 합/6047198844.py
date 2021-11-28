N = int(input())
# base case
# 최대 개수로 초기화 == 1^2으로 만드는수 == 수자체.
# ex) 12로 만드는 제곱의 합 최대수는 1^2으로 만드는 12개의 제곱의 합이다.
memo = [i for i in range(N + 1)]

for i in range(1, N + 1):
    arr = list()
    for j in range(1, int(i ** 0.5) + 1):
        arr.append(memo[i-j*j] + 1)
    memo[i] = min(arr)

print(memo[N])
