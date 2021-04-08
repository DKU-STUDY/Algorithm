#include <iostream>
using namespace std;

long long memo[1001][1001];

long long combi(int n, int k) {
	if (k == 0 || n == k)
		return 1;
	
	long long& res = memo[n][k];
	if (res) return res;
	return res = (combi(n - 1, k - 1) % 10007 + combi(n - 1, k) % 10007) % 10007;
}

int main() {
	int N;
	int K;
	cin >> N >> K;
	cout << combi(N, K);
}
