#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <limits>
#include <cstring>

using namespace std;

int n;
int m;
int A[100];
int B[100];
int cache[101][101];
const long long NEGINF = numeric_limits<long long>::min();

int LIS(int A_idx, int B_idx) {
	int &res = cache[A_idx + 1][B_idx + 1];
	if (res != -1)
		return res;

	//A와 B배열은 -무한대가 아닌 이상 같지 않다.
	//A_idx 값과 B_idx값중 큰 값을 max_element라고 한다.
	long long a = A_idx == -1 ? NEGINF : A[A_idx];
	long long b = B_idx == -1 ? NEGINF : B[B_idx];
	long long maxElement = max(a, b);

	res = 2;
	for (int nextAidx = A_idx + 1; nextAidx < n; nextAidx++)
		if (maxElement < A[nextAidx])
			res = max(res, 1 + LIS(nextAidx, B_idx));
	for (int nextBidx = B_idx + 1; nextBidx < m; nextBidx++)
		if (maxElement < B[nextBidx])
			res = max(res, 1 + LIS(A_idx, nextBidx));
	return res;
}

int main() {
	int c;
	cin >> c;
	while (c--) {
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> A[i];
		for (int i = 0; i < m; i++)
			cin >> B[i];
		memset(cache, -1, sizeof(cache));
		cout << LIS(-1, -1) - 2 << "\n";
	}
}