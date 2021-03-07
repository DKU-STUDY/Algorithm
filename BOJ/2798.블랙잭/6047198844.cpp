#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, M;

//첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
//index + 1을 선택했을때의 수와 index + 1을 선택하지 않았을때의 수
int brute_force(vector<int> &arr, int idx, int cnt, int sum) {
	//index + 1의 선택을 고려하지않는수. 이미 조건 만족. 더이상 고려할것이없다 -> base case
	if (cnt == 0 && sum <= M)
		return sum;

	//idx+1을 선택했을때의 수와 idx+1을 선택하지 않았을때의 수를 고려하는 수.
	if (cnt < 0 || sum > M || idx + 1 >= N)
		return 0;
	return max(brute_force(arr, idx + 1, cnt, sum), brute_force(arr, idx + 1, cnt - 1, sum + arr[idx + 1]));
}

int main() {
	cin >> N >> M;
	vector <int> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	int res;
	res = brute_force(arr, -1, 3, 0);
	cout << res;
}