#include <iostream>

using namespace std;

long long board[100][100];
long long memo[100][100]; //memo[y][x] : y, x 좌표에서의 개수
bool check[100][100];
int N;

long long dp(int y, int x) {
	if (x >= N || y >= N)
		return 0;
	if (y == N - 1 && x == N - 1)
		return 1;
	if (check[y][x])
		return memo[y][x];
	
	long long& res = memo[y][x];
	check[y][x] = true;
	res = dp(y + board[y][x], x) + dp(y, x + board[y][x]);
	return res;
}

int main() {
	cin >> N;
	for (int y = 0; y < N; y++)
		for (int x = 0; x < N; x++)
			cin >> board[y][x];
	cout << dp(0, 0);
}