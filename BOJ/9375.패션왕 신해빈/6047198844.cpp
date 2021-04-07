#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		map <string, int> mp;
		while (N--) {
			string a, b;
			cin >> a >> b;
			mp[b]++;
		}
		int res = 1;
		for (auto i : mp)
			res *= (i.second + 1);
		cout << res - 1 << "\n";
	}
}