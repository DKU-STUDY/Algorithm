import heapq
import sys
from collections import deque

K, N = map(int, sys.stdin.readline().split())
primes = list(map(int, sys.stdin.readline().split()))
PQ = primes.copy()

head = 0
for _ in range(N):
    head = heapq.heappop(PQ)
    for prime in primes:
        heapq.heappush(PQ, head * prime)
        if head % prime == 0:
            break
print(head)