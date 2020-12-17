#include <iostream>
#include <algorithm>

using namespace std;

int miro[1001][1001];
int memo[1001][1001];
int max_x; int max_y;

int dx[3] = { -1,0,-1 };
int dy[3] = { 0,-1,-1 };

bool check(int y, int x) {
	if (y<1 || y>max_y)
		return false;
	if (x<1 || x>max_x)
		return false;
	return true;
}

int dp(int y, int x) {
	if (memo[y][x])
		return memo[y][x];

	int &res = memo[y][x];
	for (int i = 0; i < 3; i++) {
		int check_y = y + dy[i];
		int check_x = x + dx[i];
		if (check(check_y, check_x)) {
			res = max(dp(check_y, check_x) + miro[y][x], res);
			//이부분에서 실수
			//문제 잘못읽음
		}
	}
	return res;
}

int main() {
	cin >> max_y >> max_x;
	for (int i = 1; i <= max_y; i++)
		for (int j = 1; j <= max_x; j++)
			cin >> miro[i][j];
	memo[1][1] = miro[1][1];
	cout << dp(max_y, max_x);
}