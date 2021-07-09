import sys
sys.setrecursionlimit(10000)

memo = [-1]*2001

def solution(n):
    if n <= 2:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = (solution(n-1) % 1234567 + solution(n-2) % 1234567) % 1234567
    return memo[n]