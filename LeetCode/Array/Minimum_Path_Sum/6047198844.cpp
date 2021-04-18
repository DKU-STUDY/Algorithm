typedef pair<int,pair<int,int>> P; 

class Solution {
private:
    const int INF = 987654321;
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        vector< vector<int> > dist(m,vector<int>(n,INF));
        
        priority_queue < P , vector<P>, greater<P> > pq;
        
        dist[0][0] = grid[0][0];
        pq.push({dist[0][0],{0,0}});
        
        while(!pq.empty()){
            int y = pq.top().second.first;
            int x = pq.top().second.second;
            int d = pq.top().first; // 0,0에서 y,x로 가는 최단 거리.
            pq.pop();
            
            if(d > dist[y][x])
                continue;
            
            if(y+1 < m &&(d+grid[y+1][x] < dist[y+1][x])){
                dist[y+1][x] = d + grid[y+1][x];
                pq.push({dist[y+1][x],{y+1,x}});
            }
            
            if(x+1 < n &&(d+grid[y][x+1] < dist[y][x+1])){
                dist[y][x+1] = d + grid[y][x+1];
                pq.push({dist[y][x+1],{y,x+1}});
            }
        }
        
        return dist[m-1][n-1];
    }
};