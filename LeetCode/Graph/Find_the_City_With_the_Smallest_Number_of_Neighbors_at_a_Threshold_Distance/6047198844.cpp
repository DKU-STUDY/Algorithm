class Solution {
private:
    const int INF = 987654321;
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<pair<int,int>>> edge(n);
        
        for(int i = 0; i < edges.size(); i++){
            int u = edges[i][0];
            int v = edges[i][1];
            int e = edges[i][2];
            
            edge[u].push_back({v,e});
            edge[v].push_back({u,e});            
        }

        int res_cnt = INF;
        int res_v = 0;
        
        for(int  i = 0; i < n; i++){
            vector<int> dist(n,INF);
            int here = i;
            dist[here] = 0;
            
            priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
            int cnt = 0;
            
            pq.push({dist[here],here});
            
            while(!pq.empty()){
                int here = pq.top().second;
                int d = pq.top().first;
                pq.pop();
                
                if(d > distanceThreshold)
                    break;
                
                if(d > dist[here])
                    continue;
                
                for(auto p : edge[here]){
                    int there = p.first;
                    int e = p.second;
                    
                    if(d+e < dist[there] && d+e<=distanceThreshold){
                        if(dist[there] > distanceThreshold)
                            cnt ++ ;
                        dist[there] = d+e;
                        pq.push({dist[there],there});
                    }
                }
            }    
            if(res_cnt >= cnt){
                res_cnt = cnt;
                res_v = i;
            }
        }
        return res_v;
    }
};