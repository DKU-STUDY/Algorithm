import sys
from itertools import combinations_with_replacement


def get_primes():
    is_prime = [True for _ in range(1001)]
    is_prime[0] = is_prime[1] = False

    for i in range(1001):
        if is_prime[i]:
            for j in range(i + i, 1001, i):
                is_prime[j] = False

    primes = [i for i in range(1001) if is_prime[i]]
    return primes


T = int(sys.stdin.readline().rstrip())

tests = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
sols = dict()
primes = get_primes()

for s in ç(primes, 3):
    acc = sum(s)
    if acc in tests:
        sols[acc] = s

for test in tests:
    if test in sols:
        print(' '.join(map(str, sols[test])))
    else:
        print(0)
