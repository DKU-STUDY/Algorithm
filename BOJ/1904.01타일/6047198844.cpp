#include <iostream>

using namespace std;

int dp(int n) {
	int a = 1;
	int b = 2;
	int temp;
	for (int i = 2; i <= n; i++) {
		temp = b;
		b = (a + b) % 15746;
		a = temp;
	}
	return a;
}

int main() {
	int n;
	cin >> n;
	cout << dp(n);
}