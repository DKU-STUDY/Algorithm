class Solution {
private:
    int d[3] = {-1,0,+1};
    
public:
    bool isValid(int y, int x, int n){
        return (0<=y&&y<n)&&(0<=x&&x<n);
    }
    
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid[0][0])
            return -1;
        
        int n = grid.size();
        int res = 1;
        
        if(n==1)
            return res;
        
        queue<pair<int,int> > q;
        q.push({0,0});
        
        while(!q.empty()){
            int m = q.size();
            for(int i = 0;  i < m ; i++){
                pair<int,int> cord = q.front();
                q.pop();
                if(cord.first == n-1 && cord.second == n-1)
                    return res;
                    
                for(int j = 0; j < 9; j++){
                    int ny = cord.first + d[j/3];
                    int nx = cord.second + d[j%3];
                    if(isValid(ny,nx,n)&&!grid[ny][nx]){
                        grid[ny][nx] = 1;
                        q.push({ny,nx});
                    }
                }    
            }
            res++;
        }
        return -1;
    }
};