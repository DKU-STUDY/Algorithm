#include <string>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> P;
const int INF = 9876543;

vector<int> dijk (int n , int src, vector<vector<P>> &edges){
    vector<int> dist(n+1,INF);
    
    priority_queue < P , vector<P> , greater<P> > pq;
    dist[src] = 0;
    pq.push({dist[src],src});
    
    while(!pq.empty()){
        int here = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if(d > dist[here])
            continue;
        
        for(auto p : edges[here]){
            int there = p.first;
            int e = p.second;
            
            if(dist[there] > d + e){
                dist[there] = d + e;
                pq.push({dist[there], there});
            }
        }
    }
    return dist;
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<vector<pair<int,int>>> edges(n+1);
    
    for(int i = 0; i < fares.size(); i++){
        int u = fares[i][0];
        int v = fares[i][1];
        int e = fares[i][2];
        
        edges[u].push_back({v,e});
        edges[v].push_back({u,e});
        
    }
    
    int res = INF;
    
    vector<int> distS = dijk(n,s,edges);
    for(int i = 1; i < n+1; i++){
        vector<int> distAB = dijk(n,i,edges);
        
        int tmp = distS[i] + distAB[a] + distAB[b];
        if(tmp < res)
            res = tmp;
    }
    
    return res;
}