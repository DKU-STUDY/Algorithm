#include <iostream>
#include <cstring>

#define MOD 1000000007

using namespace std;

long long cache[101];

long long tile(int n) {
	if (n <= 1)
		return 1;
	long long& res = cache[n];
	if (res != -1)
		return res;
	return res = (tile(n - 1) % MOD + tile(n - 2) % MOD) % MOD;
}

int main() {
	int C;
	cin >> C;
	int n;
	memset(cache, -1, sizeof(cache));
	while (C--) {
		cin >> n;
		tile(100);
		if (n % 2)
			cout << (tile(n) + MOD - tile(n / 2) + MOD) % MOD;
		else
			cout << (tile(n) + MOD - tile(n / 2) + MOD - tile(n / 2 - 1) + MOD) % MOD;
		cout << "\n";
	}
}
