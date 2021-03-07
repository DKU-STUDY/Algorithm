#include <iostream>
#include <cstring>

#define INT_MAX 100000
using namespace std;

int memo[51][51][51];

int w(int a, int b, int c) {
	if (a <= 0 || b <= 0 || c <= 0)
		return 1;
	if (memo[a][b][c] != -1)
		return memo[a][b][c];
	int& res = memo[a][b][c];
	if (a > 20 || b > 20 || c > 20)
		return res = w(20, 20, 20);
	if (a < b && b < c)
		return res = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
	return res = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
}

int main() {
	int a; int b; int c;
	while (1) {
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1)
			break;
		memset(memo, -1, sizeof(memo));
		//memset은 0으로 초기화할때 사용.
		cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << "\n";
	}
}