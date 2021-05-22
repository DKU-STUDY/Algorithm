#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print_fnc(int n) {
	cout << n << " ";
}

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

int main() {
	int N;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr.begin(), arr.end());
	int g = arr[1] - arr[0];
	for (int i = 2; i < N; i++)
		g = gcd(g, arr[i] - arr[i - 1]);
	//10억의 제곱근 = 3~4만
	vector<int> res;
	for (int i = 1; i * i <= g; i++) {
		if (g % i)
			continue;
		res.push_back(i);
		res.push_back(g / i);
	}
	sort(res.begin(), res.end());
	res.erase(unique(res.begin(), res.end()), res.end());
	for_each(res.begin() + 1, res.end(),print_fnc);
}