#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int com_num(int a, int b) {
	bool check[11];
	vector <int> vt;
	memset(check, false, sizeof(check));
	int res = 1;
	for (int i = 0; i < 9; i++) {
		res *= a;
		res %= 10;
		if (check[res]) {
			int size = vt.size();
			if (b % size)
				return vt[b % size - 1];
			else
				return vt[size - 1];
		}
		check[res] = true;
		vt.push_back(res);
	}
}

int main() {
	int T;
	cin >> T;
	int a, b;
	int res;
	while (T--) {
		cin >> a >> b;

		res = com_num(a, b);
		if (res)
			cout << res;
		else
			cout << 10;
		cout << "\n";
	}
}