#include <iostream>
#include <vector>

using namespace std;

int gcf(int a, int b) {
	if (b == 0)
		return a;
	return gcf(b, a % b);
}

int main() {
	int N;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	for (int i = 1; i < N; i++) {
		int f = gcf(arr[0], arr[i]);
		cout << arr[0] / f << "/" << arr[i] / f << "\n";
	}
}
