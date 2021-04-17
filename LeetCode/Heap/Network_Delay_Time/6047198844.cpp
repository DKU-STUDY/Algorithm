class Solution {
private:
    const int INF = 987654321;
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> edges(n+1);
        for(int i = 0; i < times.size(); i++){
            int u = times[i][0];
            int v = times[i][1];
            int e = times[i][2];
            edges[u].push_back({v,e});
        }
        
        vector<int> dist(n+1,INF); // check안하면 0
        priority_queue <pair<int,int>,vector<pair<int,int>>,less<pair<int,int>>> pq;
        dist[0] = 0;
        dist[k] = 0;
        pq.push({dist[k],k});
        
        while(!pq.empty()){
            int here = pq.top().second;
            int cost = pq.top().first;
            pq.pop();
            
            if(cost > dist[here])
                continue;
            
            for(auto p : edges[here]){
                int there = p.first;
                int e = p.second;
                if(cost + e < dist[there]){
                    dist[there] = cost + e;
                    pq.push({dist[there],there});
                }
            }
        }
        
        int res = *max_element(dist.begin(),dist.end());
        
        return res == INF ? -1 : res;
    }
};