#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main() {
	int N;
	cin >> N;
	int arr[101];
	bool check[101];
	memset(check, false, 1+N);
	for (int i = 1; i <= N; i++)
		cin >> arr[i];
	vector <int> res;
	for (int i = 1; i <= N; i++) {
		vector <int> vt;
		int idx = i;
		while (!check[idx]) {
			vt.push_back(idx);
			check[idx] = true;
			idx = arr[idx];
		}
		auto it = find(vt.begin(), vt.end(), idx);
		while (it != vt.end()) {
			res.push_back(*it);
			it++;
		}
	}
	sort(res.begin(), res.end());
	cout << res.size() << "\n";
	for (auto i : res) {
		cout << i << "\n";
	}
}