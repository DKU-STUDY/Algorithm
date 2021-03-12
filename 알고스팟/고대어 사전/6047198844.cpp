#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;

void makeGraph(const vector<string>& words) {
	adj = vector<vector<int> >(26, vector<int>(26, 0));
	for (int j = 1; j < words.size(); j++) {
		int i = j - 1;
		int len = min(words[j].length(), words[i].length());
		for (int k = 0; k < len; k++) {
			if (words[i][k] != words[j][k]) {
				int a = words[i][k] - 'a';
				int b = words[j][k] - 'a';
				adj[a][b] = 1;
				break;
			}
		}
	}
}

vector<int> seen, order;
void dfs(int here) {
	seen[here] = 1;
	for (int there = 0; there < adj.size(); ++there)
		if (adj[here][there] && !seen[there])
			dfs(there);
	order.push_back(here);
}

vector<int> topologicalSort() {
	int m = adj.size();
	seen = vector<int>(m, 0);
	order.clear();
	for (int i = 0; i < m; i++) if (!seen[i]) dfs(i);
	reverse(order.begin(), order.end());

	for (int i = 0; i < m; ++i)
		for (int j = i + 1; j < m; ++j)
			if (adj[order[j]][order[i]])
				return vector<int>();
	return order;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<string> words(N);
		for (int i = 0; i < N; i++)
			cin >> words[i];

		makeGraph(words);
		vector <int> res = topologicalSort();
		if (!res.empty())
			for (int i : res)
				cout << (char)(i + 'a');
		else
			cout << "INVALID HYPOTHESIS";
		cout << "\n";
	}
}