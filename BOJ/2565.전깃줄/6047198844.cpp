#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int cache[100];

int dp(vector<int>& vt, int idx,int size) {
	int& res = cache[idx];
	if (res)
		return res;
	res = 1;
	for (int dx = 1; idx + dx <= size; dx++) {
		if (vt[idx] < vt[idx + dx]) {
			res = max(res, 1 + dp(vt, idx + dx, size));
		}
	}
	return res;
}

int main() {
	int N;
	cin >> N;
	pair <int, int> p;
	vector<pair<int, int>> vt;
	while (N--) {
		cin >> p.first >> p.second;
		vt.push_back(p);
	}
	sort(vt.begin(), vt.end());
	int size = vt.size();
	vector <int> lis;
	lis.push_back(-1);
	for (int i = 0; i < size; i++) {
		lis.push_back(vt[i].second);
	}
	cout << size - (dp(lis, 0, size) - 1);
}