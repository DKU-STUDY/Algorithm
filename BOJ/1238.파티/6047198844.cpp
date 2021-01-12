//다익스트라 알고리즘 1
//#include <iostream>
//#include <vector>
//#include <queue>
//#include <climits>
//#define INF INT_MAX
//
//using namespace std;
//
//vector <pair<int, int> > edge[1001];
//
//vector <int> Dijkstra(int N, int K) {
//	priority_queue <pair<int, int> > pq;
//	vector <int> dest(N + 1, INF);
//	dest[K] = 0;
//	pq.push({ 0, K });
//	while (!pq.empty()) {
//		int cost = -pq.top().first;
//		int here = pq.top().second;
//		pq.pop();
//		if (cost > dest[here])
//			continue;
//		for (auto there : edge[here]) {
//			if (dest[there.first] > cost + there.second) {
//				dest[there.first] = cost + there.second;
//				pq.push({ -dest[there.first],there.first });
//			}
//		}
//	}
//	return dest;
//}
//
//int main() {
//	int N, M, X;
//	cin >> N >> M >> X;
//	int a, b, cost;
//	while (M--) {
//		cin >> a >> b >> cost;
//		edge[a].push_back({ b,cost });
//	}
//	vector <int> res[1001];
//	for (int i = 1; i <= N; i++) {
//			res[i] = Dijkstra(N, i);
//	}
//	int r = -1;
//	for (int i = 1; i <= N; i++) {
//		if((res[X][i]!=INF)&&(res[i][X]!=INF))
//			r = max(r, res[X][i] + res[i][X]);
//	}
//	cout << r;
//}

//다익스트라 알고리즘2
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#define INF INT_MAX

using namespace std;
vector <vector <pair<int, int> >> edge[2];

vector <int> Dijkstra(int N, int K,int num) {
	priority_queue <pair<int, int> > pq;
	vector <int> dest(N + 1, INF);
	dest[K] = 0;
	pq.push({ 0, K });
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		if (cost > dest[here])
			continue;
		for (auto there : edge[num][here]) {
			if (dest[there.first] > cost + there.second) {
				dest[there.first] = cost + there.second;
				pq.push({ -dest[there.first],there.first });
			}
		}
	}
	return dest;
}

int main() {
	int N, M, X;
	cin >> N >> M >> X;
	int a, b, cost;
	edge[0].resize(N + 1);
	edge[1].resize(N + 1);
	while (M--) {
		cin >> a >> b >> cost;
		edge[0][a].push_back({ b,cost });
		edge[1][b].push_back({ a,cost });
	}
	vector <int> res[2];
	res[0] = Dijkstra(N, X, 0);
	res[1] = Dijkstra(N, X, 1);
	int r = -1;
	for (int i = 1; i <= N; i++) {
			r = max(r, res[0][i] + res[1][i]);
	}
	cout << r;
}