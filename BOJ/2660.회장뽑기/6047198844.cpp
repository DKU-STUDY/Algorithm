#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

//해당 노드에 연결된 간선을 모두 검사한다.
bool check[51];
vector <int> edge[51];

int bfs(int node, int n) {
	int level = 0;
	memset(check + 1, false, n + 1);
	check[node] = true;
	queue <int> q;
	for (int i = 0; i < edge[node].size(); i++) {
		q.push(edge[node][i]);
		check[edge[node][i]] = true;
	}
	while (!q.empty()) {
		level++;
		int q_size = q.size();
		for (int i = 0; i < q_size; i++) {
			int node = q.front(); q.pop();
			int node_size = edge[node].size();
			for (int j = 0; j < node_size; j++) {
				if (!check[edge[node][j]]) {
					q.push(edge[node][j]);
					check[edge[node][j]] = true;
				}
			}
		}
	}
	return level;
}

bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.second != b.second)
		return a.second < b.second;
	return a.first < b.first;
}

int main() {
	int N;
	cin >> N;
	int a; int b;
	while (1) {
		cin >> a >> b;
		if (a == -1 && b == -1)
			break;
		edge[a].push_back(b);
		edge[b].push_back(a);
	}
	vector <pair<int, int> > res;
	for (int i = 1; i <= N; i++) {
		int num = bfs(i, N);
		res.push_back({ i,num });
	}
	sort(res.begin(), res.end(), compare);
	int candidate = res[0].second;
	vector <int> va;
	int num = 0;
	for (auto c : res) {
		if (c.second != candidate)
			break;
		num++;
		va.push_back(c.first);
	}
	cout << candidate << " " << num << "\n";
	for (int i : va)
		cout << i << " ";
}