from math import sqrt

N = int(input())
memo = [9999999 for _ in range(N + 1)]
# base case
for i in range(1, int(N ** 0.5) + 1):
    memo[i ** 2] = 1

for i in range(N + 1):
    for j in range(i // 2 + 1):
        memo[i] = min(memo[i], memo[i - j] + memo[j])

print(memo[N])
