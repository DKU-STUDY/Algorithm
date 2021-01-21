#include <iostream>
#include <string>

using namespace std;

//뒤의 두자리만 곱한다.
int factorial(int n) {
	long long mul = 1;
	for (int i = 1; i <= n; i++) {
		mul *= i;
		mul %= 1000000000;
		while (!(mul % 10))
			mul /= 10;
	}
	return mul % 10;
}

int main() {
	int n;
	cin >> n;
	cout << factorial(n);
}