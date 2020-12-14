#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool check[101];
vector <int> vt[101];

int bfs(int computer_num) {
	int res = 0;
	memset(check, false, sizeof(bool) * 101);
	check[1] = true;
	queue <int> q;
	q.push(1);
	while (!q.empty()) {
		int computer = q.front();
		q.pop();
		int size = vt[computer].size();
		for (int i = 0; i < size; i++) {
			if (!check[vt[computer][i]]) {
				q.push(vt[computer][i]);
				check[vt[computer][i]] = true;
				res++;
			}
		}
	}
	return res;
}

int main() {
	int computer_num;
	int line;
	cin >> computer_num;
	cin >> line;

	int line_a;
	int line_b;
	for (int i = 0; i < line; i++) {
		cin >> line_a >> line_b;
		vt[line_a].push_back(line_b);
		vt[line_b].push_back(line_a);
	}
	cout << bfs(computer_num);
}