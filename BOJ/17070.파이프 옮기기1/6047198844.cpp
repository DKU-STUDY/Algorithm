#include <iostream>
#include <cstring>

using namespace std;

int memo[17][17][3];
int arr[17][17];
int N;

int dp(int y,int x,int type) {
	if (x > N || y > N)
		return 0;
	if (x == N && y == N)
		return 1;

	int& res = memo[y][x][type];
	if (res != -1)
		return res;
	res = 0;
	//type1 가로
	if (type != 1) {
		if (!arr[y][x + 1])
			res += dp(y, x + 1, 0);
	}
	//type2 세로
	if (type != 0) {
		if (!arr[y + 1][x])
			res += dp(y + 1, x, 1);
	}
	if (!arr[y][x + 1] && !arr[y + 1][x + 1] && !arr[y + 1][x]) {
		res += dp(y + 1, x + 1, 2);
	}
	return res;
}

int main() {
	cin >> N;
	for (int y = 1; y <= N; y++)
		for (int x = 1; x <= N; x++)
			cin >> arr[y][x];
	memset(memo, -1, sizeof(memo));
	cout << dp(1, 2, 0);
}