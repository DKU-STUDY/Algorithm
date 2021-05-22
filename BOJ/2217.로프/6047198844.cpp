#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector <int> vt(N);
	for (int i = 0; i < N; i++)
		cin >> vt[i];

	sort(vt.begin(), vt.end());

	int size = vt.size();
	int res_max = 0;
	for (int i = 0; i < N; i++)
		res_max = max(res_max,vt[i] * (size - i));

	cout << res_max;
}