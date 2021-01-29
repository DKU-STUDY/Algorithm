#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lis(int idx, int N, vector <int> &seq, vector <int> &memo) {
	int& res = memo[idx + 1];
	if (res != -1)
		return res;
	res = 1;
	for (int start = idx + 1; start < N; start++) {
		if (idx == -1 || seq[idx] < seq[start])
			res = max(res, 1 + lis(start, N, seq, memo));
	}
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector <int> seq(N);
		vector <int> memo(N + 1, -1);
		for (int i = 0; i < N; i++) {
			cin >> seq[i];
		}
		cout << lis(-1, N, seq, memo) - 1 << "\n";
	}
}