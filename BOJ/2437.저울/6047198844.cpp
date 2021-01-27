#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

#define INF INT_MAX;

using namespace std;

int main() {
	int N;
	cin >> N;
	vector <int> vt(N + 1);
	vector <int> sum(N);
	for (int i = 0; i < N; i++)
		cin >> vt[i];
	vt[N] = INF;
	sort(vt.begin(), vt.end());

	int res = 0;
	for (int i = 0; i <= N; i++) {
		//res는 만들수있는 정수의 최대값이다.
		if (res + 2 <= vt[i]) {
			cout << res + 1;
			return 0;
		}
		res += vt[i];
	}
}