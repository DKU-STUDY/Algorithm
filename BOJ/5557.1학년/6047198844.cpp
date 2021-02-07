#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int cache[100][20];
int arr[100];
int N;

int dp(int idx, int sum) {
	if (sum < 0 || sum>20)
		return 0;
	if (idx == N - 2)
		return sum == arr[N - 1];
	int &res = cache[idx][sum];
	if (res != -1)
		return res;
	res = 0;
	res = dp(idx + 1, sum + arr[idx + 1]) + dp(idx + 1, sum - arr[idx + 1]);
	return res;
}

int main() {
	memset(cache, -1, sizeof(cache));
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> arr[i];	
	cout << dp(0, arr[0]);
}