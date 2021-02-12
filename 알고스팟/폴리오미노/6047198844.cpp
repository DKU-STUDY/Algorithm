#include <iostream>
#include <cstring>

#define ll long long
using namespace std;

long long memo[101][101];

ll dp(int used, int remain) {
	if (remain == 0)
		return 1;
	ll &res = memo[used][remain];
	if (res != -1)
		return res;
	res = 0;
	for (int cnt = 1; cnt <= remain; cnt++) {
		int mul = used ? (used + cnt - 1) : 1;
		res += (mul * dp(cnt, remain - cnt)% 10000000);
	}
	return res % 10000000;
}

int main() {
	int C;
	cin >> C;
	int n;
	memset(memo, -1, sizeof(memo));
	while (C--) {
		cin >> n;
		cout << dp(0, n) << "\n";
	}
}