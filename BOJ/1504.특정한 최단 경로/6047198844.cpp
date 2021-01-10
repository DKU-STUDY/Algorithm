#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <climits>
#define INF 987654321
using namespace std;


vector <pair< int,int > > graph[801];

vector <int> dijkstra(int N,int v) {
	vector <int> dest(N + 1, INF);
	priority_queue <pair<int, int> > pq;
	pq.push({ 0,v });
	dest[v] = 0;
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		if (cost > dest[here])
			continue;
		for (auto node : graph[here]) {
			if (dest[node.first] > cost + node.second) {
				dest[node.first] = cost + node.second;
				pq.push({ -dest[node.first], node.first });
			}
		}
	}
	return dest;
}

int main() {
	int N, E;
	cin >> N >> E;
	int a, b, c;
	while (E--) {
		cin >> a >> b >> c;
		graph[a].push_back({ b,c });
		graph[b].push_back({ a,c });
	}
	int v1, v2;
	cin >> v1 >> v2;

	vector <int> start_di = dijkstra(N, 1);
	vector <int> dist_v1 = dijkstra(N, v1);
	vector <int> dist_v2 = dijkstra(N, v2);
	//오버플로우.
	int cnt = INF;
	int res;
	// 1 -> v1 -> v2 -> N
	// 1 -> v2 -> v1 -> N

	res = min(start_di[v1] + dist_v1[v2] + dist_v2[N], start_di[v2] + dist_v2[v1] + dist_v1[N]);
	if (res < INF && res > 0)
		cout << res;
	else
		cout << "-1";
}

//edge가 반드시 최저라는 보장이 없다.