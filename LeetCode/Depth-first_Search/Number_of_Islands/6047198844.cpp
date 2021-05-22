class Solution {
private:
    int dy[4] = {-1,+1, 0, 0};
    int dx[4] = { 0, 0,-1,+1};
public:
    void dfs(int y, int x, const int max_y, const int max_x, vector<vector<char>>& grid){
        grid[y][x] = '0';
        for(int d = 0 ; d < 4; d++){
            int there_y = y + dy[d];
            int there_x = x + dx[d];
            if(0 <= there_y&&
               there_y<max_y&&
               0 <= there_x&&
               there_x<max_x&&
               grid[there_y][there_x] == '1')
               dfs(there_y,there_x,max_y,max_x,grid);
        }
    }
    
    int dfsAll(vector<vector<char>>& grid){
        int res = 0;
        int max_y = grid.size();
        int max_x = grid[0].size();
        for(int y=0; y < max_y; y++)
            for(int x=0; x < max_x; x++)
                if(grid[y][x] == '1'){
                    dfs(y, x, max_y, max_x, grid);
                    res++;
                }
        return res;
    }
    
    int numIslands(vector<vector<char>>& grid) {
        return dfsAll(grid);
    }
};
