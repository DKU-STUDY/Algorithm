class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for x in range(n)] for y in range(m)]
        memo[m-1][n-1] = 1
        
        #y,x에서의 경우의수
        def dfs(y,x):
            #예외처리
            if not (0 <= y < m and 0 <= x < n):
                return 0
            
            #메모이제이션
            if memo[y][x] != -1:
                return memo[y][x]
            
            memo[y][x] = dfs(y+1,x) + dfs(y,x+1)
            return memo[y][x]
        
        return dfs(0,0)