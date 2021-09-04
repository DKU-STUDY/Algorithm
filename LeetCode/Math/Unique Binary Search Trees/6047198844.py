class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = 2*memo[i-1] + memo[i-2]**2
        print(memo)
        return memo[n]