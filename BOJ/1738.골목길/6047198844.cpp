#include <iostream>
#include <vector>
#include <climits>
#include <stack>

#define INF INT_MAX
using namespace std;

bool bellman(vector < vector<pair<int, int> >> &vt, vector <int> &res) {
	bool flag = true;
	int N = vt.size();
	vector <int> dist(N,INF);
	
	dist[0] = 0;
	//v w u
	//v는 0.
	//dist[w]는 v와 w간의 최단거리

	for (int i = 0; i < N; i++) {
		for (int w = 0; w < N; w++) {
			for (auto k : vt[w]) {
				int u = k.first; // 정점
				int w_u_cost = k.second; // w에서 u까지가는 경로.
				if (dist[w]!=INF&&dist[u] > dist[w] + w_u_cost) {
					dist[u] = dist[w] + w_u_cost;
					res[u] = w;
					if (i == N - 1) {
						for (auto r : vt[u]) {
							if (r.first == N - 1)
								flag = false;
						}
					}
				}
			}
		}
	}
	if (dist[N - 1] == INF) {
		cout << "뭐임";
	}
		//flag = false;
	return flag;
}

int main() {
	int n, m;
	cin >> n >> m;
	vector < vector<pair<int,int> >> vt(n);
	vector <int> res(n);
	int u, v, w;
	for (int i = 0; i < m; i++) {
		cin >> u >> v >> w;
		vt[u - 1].push_back({ v - 1,-w });
	}
	if (bellman(vt, res)) {
		stack <int> s;
		s.push(n);
		for (int idx = n - 1,cnt = 0; res[idx]; idx = res[idx],cnt++) {
			s.push(res[idx] + 1);
		}
		s.push(1);
		while (!s.empty()) {
			cout << s.top() << " ";
			s.pop();
		}
		return 0;
	}
	cout << -1;
}