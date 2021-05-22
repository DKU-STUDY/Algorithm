#include <iostream>
#include <vector>
#include <climits>
#define P pair<int,long long>
#define INF INT_MAX
#define LL long long
using namespace std;

void Bellman_ford(int N,vector <vector<P>> &adj) {
	vector <LL> dist(N, INF);
	dist[0] = 0;
	bool infinite_loop = false;
	for (int i = 0; i < N; i++) {
		for (int u = 0; u < N; u++) {
			for (auto p : adj[u]) {
				int v = p.first;
				LL cost = p.second;
				if (dist[u] != INF && dist[v] > dist[u] + cost) {
					dist[v] = dist[u] + cost;
					if (i == N - 1)
						infinite_loop = true;
				}
			}
		}
	}
	if (infinite_loop) {
		cout << -1;
		return;
	}

	for (int i = 1; i < N; i++) {
		if (dist[i] == INF)
			cout << "-1";
		else
			cout << dist[i];
		cout << "\n";
	}
}


int main() {
	int N, M;
	cin >> N >> M;
	vector <vector<P>> adj(N);
	int A, B, C;
	for (int i = 0; i < M; i++) {
		cin >> A >> B >> C;
		//출발 -> 도착 -> 비용
		adj[A - 1].push_back({ B - 1,C });
	}
	Bellman_ford(N, adj);
}