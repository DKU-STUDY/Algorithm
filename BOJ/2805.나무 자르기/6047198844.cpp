#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	vector<long long> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	sort(arr.begin(), arr.end(), greater<long long>());
	
	long long start = 0;
	long long end = arr[0];
	
	while (start + 1 < end) {
		long long mid = (start + end) / 2;

		long long h = 0;
		for (int i = 0; i < N; i++) {
			long long dif = arr[i] - mid;
			if (dif <= 0)
				break;
			h += dif;
		}

		if (h < M) {
			end = mid;
		}
		else {
			start = mid;
		}
	}

	cout << start;
}