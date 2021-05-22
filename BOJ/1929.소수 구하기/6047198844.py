prime = [True] * 10000001  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 10000001):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 10000001, n):
                prime[m] = False


sieve()
M , N = map(int, input().split())
for _ in range(M,N+1):
    if prime[_]:
        print(_)