import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
N = int(sys.stdin.readline())
for i in range(len(primes) - 1):
    mul = primes[i] * primes[i+1]
    if mul > N:
        print(mul)
        exit()

