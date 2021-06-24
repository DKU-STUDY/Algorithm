from collections import defaultdict
from functools import lru_cache

def solution(n, money):
    #0인경우 1. 그외의 경우 아직정해지지 않았으므로 0
    dp = [1] + [0] * n
    
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    return dp[n] % 1000000007
    
    
'''
시간초과나는 이유?

    answer = 0
    money.sort()
    
    #memo[idx][n]
    memo = [[-1 for _ in range(0,n+1)] for _ in range(0,len(money))]
    
    #경우의 수를 반환한다.
    def dfs(cur, n):
        if n == 0:
            return 1
        
        if memo[cur][n] != -1:
            return memo[cur][n]
        
        memo[cur][n] = 0
        for idx in range(cur,len(money)):
            if n-money[idx] < 0:
                break
            memo[cur][n] = (memo[cur][n] + dfs(idx, n-money[idx]) % 1000000007) % 1000000007  
        return memo[cur][n]
        
    return dfs(0, n) % 1000000007
'''