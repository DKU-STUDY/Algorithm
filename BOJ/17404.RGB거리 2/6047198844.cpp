// d[N][0] = 1번집을 제외하고 N번째 집을 빨강으로 칠했을때 최대값 d[N][0] = max(d[N-1][1],d[N-1][2])
// d[N][1] = 1번집을 제외하고 N번째 집을 초록으로 칠했을때 최대값 d[N][1] = max(d[N-1][0],d[N-1][2])
// d[N][2] = 1번집을 제외하고 N번째 집을 파랑으로 칠했을때 최대값 d[N][2] = max(d[N-1][0],d[N-1][1])

#include <iostream>
#include <algorithm>
#define MAX 2000000
using namespace std;

int arr[1001][3];
int d[1001][3];

int ans = MAX;
int dp(int n) {
	for (int i = 0; i < 3; i++) {
		d[1][0] = MAX; d[1][1] = MAX; d[1][2] = MAX;
		d[1][i] = arr[1][i];

		for (int j = 2; j <= n; j++) {
			d[j][0] = min(d[j - 1][1], d[j - 1][2]) + arr[j][0];
			d[j][1] = min(d[j - 1][0], d[j - 1][2]) + arr[j][1];
			d[j][2] = min(d[j - 1][0], d[j - 1][1]) + arr[j][2];
		}

		for (int k = 0; k <= 2; k++) {
			if (i != k) {
				ans = min(ans, d[n][k]);
			}
		}
	}
	return ans;
}

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
	}
	cout << dp(N);
}