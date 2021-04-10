#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, C;
	cin >> N >> C;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr.begin(), arr.end());

	//간격에 대해서 이분 탐색
	int begin = 1;
	int end = arr[N - 1] - arr[0] + 1;
	
	while (begin + 1 < end) {
		int mid = (begin + end) / 2;
		int tmp = arr[0];
		int res = 1;
		while (1) {
			vector<int>::iterator it = lower_bound(arr.begin(), arr.end(), tmp + mid);
			if (it == arr.end())
				break;
			else
				res++;
			tmp = *it;
		}

		if (res < C) {
			end = mid;
		}
		else {
			begin = mid;
		}
	}

	cout << begin;
}