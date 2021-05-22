prime = [True] * 10000001  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 10000001):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 10000001, n):
                prime[m] = False


sieve()
N = int(input())
for i in range(2, N+1):
    if(N == 1):
        break
    if prime[i]:
        while not N % i:
            N /= i
            print(i)
