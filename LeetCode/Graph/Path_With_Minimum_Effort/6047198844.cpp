typedef pair<int,pair<int,int>> P;

class Solution {
private:
    int dy[4] = {0,1,0,-1};
    int dx[4] = {-1,0,1,0};
    const int INF = 987654321;
public:
    bool isValid(int y, int x, int yn, int xn){
        return (0<=y&&y<yn)&&(0<=x&&x<xn);
    }
    
    
    int minimumEffortPath(vector<vector<int>>& heights) {
        priority_queue<P, vector<P>, greater<P> > pq;
        int yn = heights.size();
        int xn = heights[0].size();
        vector<vector<int>> mef(yn,vector<int>(xn,INF));
        mef[0][0] = 0;
        pq.push({mef[0][0],{0,0}});
        
        while(!pq.empty()){
            P tmp = pq.top(); pq.pop();
            int y = tmp.second.first;
            int x = tmp.second.second;
            int effort = tmp.first;
            
            if(mef[y][x] < effort)
                continue;
            
            for(int i = 0; i < 4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];
                
                if(isValid(ny,nx,yn,xn)){
                    int dif = abs(heights[ny][nx] - heights[y][x]);
                    int r = max(effort,dif);
                    
                    if(mef[ny][nx] > r){
                        mef[ny][nx] = r;
                        pq.push({mef[ny][nx],{ny,nx}});
                    }
                }
            }
            
        }
        
        return mef[yn-1][xn-1];
    }
};
