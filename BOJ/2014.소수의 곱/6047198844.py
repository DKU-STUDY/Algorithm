import sys
from collections import deque

K, N = map(int, sys.stdin.readline().split())
primes = list(map(int, sys.stdin.readline().split()))
primes.sort()

DQ = deque(primes)

head = 0
for _ in range(N-1):
    head = DQ.popleft()
    for prime in primes:
        DQ.append(head * prime)

        if head % prime == 0:
            break
print(head)