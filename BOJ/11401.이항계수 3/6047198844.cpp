#include <iostream>
#include <vector>
#define LL long long
using namespace std;

LL Factorial(int N,vector<LL> &memo) {
	if (memo[N])
		return memo[N];
	return memo[N] = N * Factorial(N - 1, memo) % 1000000007;
}

LL divide_and_conquer(int A, int P) {
	if (P == 1)
		return A;
	LL half = divide_and_conquer(A, P / 2) % 1000000007;
	if (P % 2)
		return ((half * half) % 1000000007 * A) % 1000000007;
	return half * half % 1000000007;
}

int main() {
	int N; int K;
	cin >> N >> K;
	vector<LL> memo(N + 1, 0);
	memo[0] = memo[1] = 1;
	LL N_fact = Factorial(N, memo);
	LL K_fact = Factorial(K, memo);
	LL N_minus_K_fact = Factorial(N - K, memo);
	LL res = (N_fact * divide_and_conquer(K_fact, 1000000007 - 2) % 1000000007 * divide_and_conquer(N_minus_K_fact, 1000000007 - 2)) % 1000000007;
	cout << res;
}