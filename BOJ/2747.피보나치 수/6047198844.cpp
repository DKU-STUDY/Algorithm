#include <iostream>

int memo[46] = { 0,1 };
using namespace std;

//0¹ø¤Š 0 1¹øÂ° 1
int dp(int n) {
	if (n <= 0)
		return 0;
	if (memo[n])
		return memo[n];
	int& res = memo[n];
	res = dp(n - 1) + dp(n - 2);
	return res;
}

int main() {
	int n;
	cin >> n;
	cout << dp(n);
}