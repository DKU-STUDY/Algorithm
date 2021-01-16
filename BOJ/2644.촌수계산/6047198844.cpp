#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector <int> vt[101];
bool check[101];

int bfs(int x, int y) {
	queue <int> q;
	q.push(x);
	check[x] = true;
	int cnt = 0;
	int q_size;
	while (!q.empty()) {
		q_size = q.size();
		while (q_size--) {
			int point = q.front();
			q.pop();
			int point_size = vt[point].size();
			if (point == y)
				return cnt;
			for (int i = 0; i < point_size; i++) {
				if (!check[vt[point][i]]) {
					q.push(vt[point][i]);
					check[vt[point][i]] = true;
				}
			}
		}
		cnt++;
	}
	return -1;
}

int main() {
	int n;
	cin >> n;
	int a; int b;
	cin >> a >> b;
	int m;
	cin >> m;
	int x; int y;
	while (m--) {
		cin >> x >> y;
		vt[x].push_back(y);
		vt[y].push_back(x);
	}
	cout << bfs(a, b);
}