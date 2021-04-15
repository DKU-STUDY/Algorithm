class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        int src = start;
        int dst = end;
        
        vector< vector<pair<int,double>>> edg(n);
        
        for(int i = 0; i < edges.size(); i++){
            int u = edges[i][0];
            int v = edges[i][1];
            double d = succProb[i];
            
            edg[u].push_back({v,d});
            edg[v].push_back({u,d});
        }
        
        
        priority_queue <pair<double,int>> pq;
        vector<double> dist(n,0);
        dist[src] = 1;
        pq.push({dist[src],src});
        
        while(!pq.empty()){
            pair<double,int> p = pq.top(); pq.pop();
            int here = p.second;
            double adj = p.first;
            
            if(dist[here] > adj)
                continue;
            
            for(auto e : edg[here]){
                int there = e.first;
                double d = e.second;
                if(dist[there] < adj * d){
                    dist[there] = adj * d;
                    pq.push({dist[there],there});
                }
            }
        }
        
        return dist[dst];
    }
};

//자료형 주의자료형 주의