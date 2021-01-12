#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int memo[101][100001];
vector <pair <int, int> > vt = { {0,0} };

int main() {
	int N;
	int K;
	cin >> N >> K;
	int a;
	int b;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		vt.push_back({ a,b });
	}
	for (int i = 1; i <= N; i++) {
		for (int k = 1; k < vt[i].first; k++) {
			memo[i][k] = memo[i - 1][k];
		}
		for (int j = vt[i].first; j <= K; j++) {
			memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - vt[i].first] + vt[i].second);
		}
	}
	cout << memo[N][K];
}