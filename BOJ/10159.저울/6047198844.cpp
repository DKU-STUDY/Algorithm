#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

#define INF INT_MAX

using namespace std;

void floyd(vector < vector<int> > &vt,int N){
	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i != j && vt[i][k] != INF && vt[k][j] != INF) {
					vt[i][j] = 1;
				}
			}
		}
	}
}

int main() {
	int N;
	cin >> N;
	vector < vector<int> > vt(N + 1, vector<int>(N + 1, INF));
	for (int i = 1; i <= N; i++)
		vt[i][i] = 0;
	int M;
	cin >> M;
	int i, j;
	while (M--) {
		cin >> i >> j;
		vt[i][j] = 1;
	}
	floyd(vt, N);
	for (int i = 1; i <= N; i++) {
		int res = 0;
		for (int j = 1; j <= N; j++) {
			if (vt[i][j] == INF&& vt[j][i] == INF) {
				res++;
			}
		}
		cout << res << "\n";
	}

}