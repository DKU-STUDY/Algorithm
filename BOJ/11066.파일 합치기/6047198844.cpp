#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int cache[500][500];
int page[500];

//파일i부터 파일j까지의 파일을 "합쳤을때" 발생하는 비용
int dp(int i, int j) {
	//합칠수가없다 -> 즉 0의 비용이 발생한다, 합칠수가없다.
	if (i == j)
		return 0;
	int& res = cache[i][j];
	if (res != -1)
		return res;

	int sum = 0;
	//i부터 j까지 나누어서 분할 정복한 뒤 계산한다. 이때 sum은 dp(i,k)와 dp(k+1,j)가 합쳐졌을때 드는 비용이다.
	for (int k = i; k <= j; k++)
		sum += page[k];

	int tmp;
	for (int k = i; k+1 <= j; k++) {
		tmp = (dp(i, k) + dp(k + 1, j) + sum);
		if (res == -1 || tmp < res)
			res = tmp;
	}
	return res;
}
int main() {
	int T, K, temp;
	cin >> T;
	while (T--) {
		memset(cache, -1, sizeof(cache));
		memset(page, 0, sizeof(page));
		cin >> K;
		for (int i = 0; i < K; i++)
			cin >> page[i];
		cout << dp(0, K - 1) << "\n";
	}
}
