#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr.begin(), arr.end());
	cout << arr.front() * arr.back();
}