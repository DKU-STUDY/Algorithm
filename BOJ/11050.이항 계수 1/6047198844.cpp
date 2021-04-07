#include <iostream>

using namespace std;

int combi(int N, int K) {
	if (K == 0)
		return 1;
	if (N == K)
		return 1;
	return combi(N - 1, K) + combi(N - 1, K - 1);
}

int main() {
	int N;
	int K;
	cin >> N >> K;
	cout << combi(N, K);
}