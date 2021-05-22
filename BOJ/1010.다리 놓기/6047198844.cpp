
#include <iostream>
#include <vector>

using namespace std;
//�̾ƾ��ϴ� �� : n / ��ü �� : c

int memo[31][31];
int combi(int n, int c) {
	int& res = memo[n][c];
	if (res)
		return res;

	if (n==0 || n == c)
		return res = 1;
	return res = combi(n - 1, c - 1) + combi(n, c - 1);
}

int main() {
	int T;
	cin >> T;
	while (T--) {
		int n, c;
		cin >> n >> c;
		cout << combi(n, c) << "\n";
	}
}
