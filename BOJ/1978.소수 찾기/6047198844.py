prime = [True] * 1001  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 1001):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 1001, n):
                prime[m] = False


sieve()
T = int(input())
res = 0
for n in map(int, input().split()):
    if prime[n]:
        res += 1
print(res)
