#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int K, N;
	cin >> K >> N;
	vector<long long> arr(K);
	for (int i = 0; i < K; i++)
		cin >> arr[i];
	sort(arr.begin(), arr.end());

	long long begin = 1;
	long long end = arr[K - 1] + 1;

	while (begin+1 < end) {
		long long mid = (begin + end) / 2;

		int res = 0;
		for (int i = K-1; i >= 0; i--) {
			int _ = arr[i] / mid;
			if (_ == 0)
				break;
			else
				res += _;
		}

		if (res < N) {
			end = mid;
		}
		else {
			begin = mid;
		}
	}
	cout << begin;
}

// 2147483647