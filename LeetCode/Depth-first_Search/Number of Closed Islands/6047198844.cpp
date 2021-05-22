class Solution {
private:
    int dy[4] = {-1,0,0,+1};
    int dx[4] = {0,-1,+1,0};
public:
    bool isValid(int y, int x, int yn, int xn){
        return (y >= 0 && y < yn) && (x >=0 && x < xn);
    }
    
    bool dfs(int y, int x, int yn, int xn, vector<vector<int>>& grid){
        bool flag = true;
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            
            if(isValid(ny, nx, yn, xn)){        
                if(!grid[ny][nx]){
                    grid[ny][nx] = 1;
                    if(!dfs(ny, nx, yn, xn, grid))
                        flag = false;
                }
            }else{
                flag = false;
            }
        }
        return flag;
    }
    
    int closedIsland(vector<vector<int>>& grid) {
        int res = 0;
        int yn = grid.size();
        int xn = grid[0].size();
        for(int y = 0; y < yn; y++){
            for(int x = 0; x < xn; x++){
                if(!grid[y][x]&&dfs(y,x,yn,xn,grid))
                    res ++;
            }
        }
        return res;
    }
};