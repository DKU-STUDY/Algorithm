import sys
from collections import defaultdict
from itertools import combinations, combinations_with_replacement

is_prime = [True for _ in range(1001)]
is_prime[0] = is_prime[1] = False

for i in range(1001):
    if is_prime[i]:
        for j in range(i+i,1001,i):
            is_prime[j] = False

primes = [i for i in range(1001) if is_prime[i]]

T = int(sys.stdin.readline().rstrip())
tests = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
sols = defaultdict(tuple)

for s in combinations_with_replacement(primes, 3):
    acc = sum(s)
    if acc in tests:
        sols[acc] = tuple(s)

for test in tests:
    print(sols[test])

