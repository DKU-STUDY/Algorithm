//1000000007
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int memo[101];

long long dp(int n) {
	if (n == 1 || n == 2)
		return n;
	if (memo[n] != -1)
		return memo[n] % 1000000007;
	return memo[n] = (dp(n - 1) % 1000000007 + dp(n - 2) % 1000000007) % 1000000007;
}

int main() {
	int C,N;
	cin >> C;
	memset(memo, -1, sizeof(memo));
	while (C--) {
		cin >> N;
		cout << dp(N) << "\n";
	}
}