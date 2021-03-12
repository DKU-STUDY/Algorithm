#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
void makeGraph() {
	int N;
	cin >> N;
	adj = vector<vector<int> >(N + 1);
	int M;
	cin >> M;
	int A, B;
	while (M--) {
		cin >> A >> B;
		adj[A].push_back(B);
	}
	return;
}

vector<int> order;
vector<int> seen;
void dfs(int here) {
	seen[here] = 1;
	for (int there : adj[here])
		if (!seen[there])
			dfs(there);
	order.push_back(here);
}

vector<int> topologicalSort() {
	int N = adj.size();
	seen = vector<int>(N, 0);
	order.clear();
	for (int i = 1; i < N; i++) if (!seen[i])dfs(i);
	reverse(order.begin(), order.end());
	return order;
}


int main() {
	makeGraph();
	vector <int> res = topologicalSort();
	for (int i : res)
		cout << i << " ";
}