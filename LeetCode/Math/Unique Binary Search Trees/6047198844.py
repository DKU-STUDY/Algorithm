class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0]*(n+2)
        memo[1] = 1
        for i in range(2, n+2):
            for j in range(i):
                memo[i] += memo[j]*memo[i-j]
        return memo[n+1]