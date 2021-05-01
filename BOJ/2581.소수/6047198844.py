prime = [True] * 10001  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 10001):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 10001, n):
                prime[m] = False


sieve()
M = int(input())
N = int(input())

prime_list = [i for i in range(M,N+1) if prime[i]]
if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)