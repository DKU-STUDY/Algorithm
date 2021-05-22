#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int N;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr.begin(), arr.end());

	int M;
	cin >> M;
	while (M--) {
		int _;
		cin >> _;
		int idx = lower_bound(arr.begin(), arr.end(), _) - arr.begin();
		int res = 0;
		if (idx != arr.size()&&arr[idx]==_) {
			int eIdx = upper_bound(arr.begin(), arr.end(), _) - arr.begin();
			res = eIdx - idx;
		}
		cout << res << " ";
	}
}