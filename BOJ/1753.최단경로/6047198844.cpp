#include <iostream>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;
#define INF INT_MAX

vector <pair<int, int> > edge[20001];

vector <int> dijkstra(int V, int K) {
	vector <int> dist(V + 1, INF);
	dist[K] = 0;
	priority_queue <pair<int, int> > pq;
	pq.push({ 0,K });
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		if (cost > dist[here])
			continue;
		for (auto neigh : edge[here]) {
			if (dist[neigh.first] > cost + neigh.second) {
				dist[neigh.first] = cost + neigh.second;
				pq.push({ -dist[neigh.first] ,neigh.first });
			}
		}
	}
	return dist;
}

int main() {
	int V, E;
	int K;
	int u, v, w;
	cin >> V >> E;
	cin >> K;
	while (E--) {
		cin >> u >> v >> w;
		edge[u].push_back({ v,w });
	}
	vector <int> dist = dijkstra(V, K);
	for (int i = 1; i <= V; i++) {
		if (dist[i] == INF)
			cout << "INF";
		else
			cout << dist[i];
		cout << "\n";
	}
		
}