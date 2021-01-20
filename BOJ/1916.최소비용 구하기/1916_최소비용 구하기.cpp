#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int Dijkstra(int start, int end, vector <vector<pair<int, int>>> cost) {
	//start to everywhere의 최소값.
	vector <int> dist(cost.size() + 1, INT_MAX);
	priority_queue<pair<int, int>> pq;
	pq.push({ 0,start });
	dist[start] = 0;
	while (!pq.empty()) {
		int mininum_cost = -pq.top().first;
		int that_vertex = pq.top().second;
		pq.pop();
		if (mininum_cost > dist[that_vertex])
			continue;
		for (auto p : cost[that_vertex]) {
			if (mininum_cost + p.first < dist[p.second]) {
				dist[p.second] = mininum_cost + p.first;
				pq.push({ -dist[p.second] ,p.second });
			}
		}
	}
	return dist[end];
}

int main() {
	int N;
	cin >> N;
	vector <vector<pair<int, int>>> cost;
	cost.resize(N + 1);
	int M;
	cin >> M;
	int from_city;
	int to_city;
	int bus_cost;
	for (int i = 0; i < M; i++) {
		cin >> from_city >> to_city >> bus_cost;
		cost[from_city].push_back({ bus_cost,to_city });
	}
	int res_from_city;
	int res_to_city;
	cin >> res_from_city >> res_to_city;
	cout << Dijkstra(res_from_city, res_to_city, cost);
}