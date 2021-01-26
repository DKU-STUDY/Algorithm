#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

#define INF INT_MAX

using namespace std;

void floyd(vector<vector<int>> &vt,int n) {
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (vt[i][k] != INF && vt[k][j] != INF && i != j)
					vt[i][j] = min(vt[i][j], vt[i][k] + vt[k][j]);
	}
	return;
}

int main() {
	int n,m;
	cin >> n;
	vector <vector<int>> vt(n + 1, vector<int>(n + 1, INF));
	cin >> m;
	int a, b, c;
	while (m--) {
		cin >> a >> b >> c;
		vt[a][b] = min(vt[a][b], c);
	}

	floyd(vt, n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (vt[i][j] == INF)
				cout << 0;
			else
				cout << vt[i][j];
			cout << " ";
		}
		cout << "\n";
	}
}