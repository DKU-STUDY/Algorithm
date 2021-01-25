#include <iostream>
#include <vector>
#include <climits>
#include <queue>

#define INF INT_MIN

using namespace std;

// u v w
// start_city에서 v까지 가는 비용

vector <long long> dist(100, INF);

bool bellman_ford(int start_city, int end_city, vector <vector<pair<int, int>>>& cost, vector <int>& earn) {
	int N = earn.size();

	vector<bool> visit(N, false);
	queue<int> vertex;

	dist[start_city] = earn[start_city];
	for (int i = 0; i < N; i++) {
		for (int v = 0; v < N; v++) {
			for (auto p : cost[v]) {
				int w = p.first;
				int v_w_cost = p.second + earn[w];
				if (dist[v] != INF && (dist[w] < dist[v] + v_w_cost)) {
					dist[w] = dist[v] + v_w_cost;
					if (i == N - 1) {
						if (!visit[w]) {
							if (w == end_city)
								return false;
							visit[w] = true;
							vertex.push(w);
							while (!vertex.empty()) {
								int check_vertex = vertex.front();
								vertex.pop();
								for (auto q : cost[check_vertex]) {
									if (!visit[q.first]) {
										if (q.first == end_city)
											return false;
										visit[q.first] = true;
										vertex.push(q.first);
									}
								}
							}
							
						}
					}
				}
			}
		}
	}
	return true;
}

int main() {
	int N, start_city, end_city, edge_num;
	cin >> N >> start_city >> end_city >> edge_num;
	vector <vector<pair<int, int>>> cost(N);

	int u, v, k;
	//비용을 입력받는다.
	while (edge_num--) {
		cin >> u >> v >> k;
		cost[u].push_back({ v,-k });
	}

	vector <int> earn(N);
	for (int i = 0; i < N; i++)
		cin >> earn[i];

	bool res = bellman_ford(start_city, end_city, cost, earn);

	if (res) {
		if (dist[end_city] == INF)
			cout << "gg";
		else
			cout << dist[end_city];
		return 0;
	}
	cout << "Gee";
}