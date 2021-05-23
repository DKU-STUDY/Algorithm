class Solution:
    def dfs_sol(self, y: int, x: int, grid: List[List[str]]):
        grid[y][x] = "0"
        
        for dy, dx in (-1,0), (1,0), (0,1), (0,-1):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == "1":
                self.dfs_sol(ny,nx,grid)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    res += 1
                    self.dfs_sol(y,x,grid)
        return res

#숫자가 아닌 문자열임.
#if문 개행?