#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

long long cache[100][21];
int arr[100];
int N;

long long dp(int idx, int sum) {
	if (sum < 0 || sum>20)
		return 0;
	if (idx == N - 2)
		return sum == arr[N - 1];
	long long& res = cache[idx][sum];
	if (res != -1)
		return res;
	res = 0;
	res = dp(idx + 1, sum + arr[idx + 1]) + dp(idx + 1, sum - arr[idx + 1]);
	return res;
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < 21; j++)
			cache[i][j] = -1;

	for (int i = 0; i < N; i++)
		cin >> arr[i];
	cout << dp(0, arr[0]);
}
