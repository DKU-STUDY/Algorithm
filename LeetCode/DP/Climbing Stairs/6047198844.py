class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]

        def dp(n):
            if n <= 2:
                return n
            
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        return dp(n)