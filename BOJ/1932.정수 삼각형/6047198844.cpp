#include <iostream>
#include <algorithm>

using namespace std;
int arr[501][501];
int memo[501][501];

int bottom_up(int n) {
	memo[1][0] = arr[1][0];
	for (int j = 2; j <= n; j++) {
		for (int i = 0; i < j; i++) {
			if (i != 0)
				memo[j][i] = memo[j - 1][i - 1];
			if (i != n - 1)
				memo[j][i] = max(memo[j][i], memo[j - 1][i]);
			memo[j][i] += arr[j][i];
		}
	}
	int res = 0;
	for (int i = 0; i < n; i++) {
		res = max(res, memo[n][i]);
	}
	return res;
}

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			cin >> arr[i][j];
		}
	}
	cout << bottom_up(n);
}