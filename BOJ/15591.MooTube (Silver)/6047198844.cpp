#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int node[5001];
bool check[5001];
vector <pair<int, int>> edge[5001];

void dfs(int n) {
	check[n] = true;
	int edge_size = edge[n].size();
	for (int i = 0; i < edge_size; i++) {
		if (!check[edge[n][i].first]) {
			node[edge[n][i].first] = !node[n] ? edge[n][i].second :
				node[n] < edge[n][i].second ? node[n] : edge[n][i].second;
			dfs(edge[n][i].first);
		}
	}
	return;
}

int main() {
	int N;
	int Q;
	cin >> N >> Q;
	int p;
	int q;
	int r;
	for (int i = 0; i < N-1; i++) {
		cin >> p >> q >> r;
		edge[p].push_back({ q,r });
		edge[q].push_back({ p,r });
	}
	int k;
	int v;
	for (int i = 0; i < Q; i++) {
		memset(node, 0, sizeof(node));
		memset(check, false, sizeof(check));
		cin >> k >> v;
		dfs(v);
		cout << count_if(node + 1, node + N + 1, [=](int elem) { return elem >= k; }) << "\n";
	}
}