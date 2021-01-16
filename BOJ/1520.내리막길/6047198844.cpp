#include <iostream>
#include <cstring>

using namespace std;

int arr[500][500];
int memo[500][500];
bool check[500][500];
int dx[4] = {-1,+1, 0, 0};
int dy[4] = { 0, 0,-1,+1};
int M;
int N;

bool check_arr(int y, int x) {
	if (y < 0 || y >= M)
		return false;
	if (x < 0 || x >= N)
		return false;
	if (check[y][x]&&memo[y][x]==-1)
		return false;
	return true;
}

int dfs(int y, int x) {
	if (memo[y][x] != -1)
		return memo[y][x];
	if (y == M - 1 && x == N - 1)
		return 1;

	int res = 0;
	for (int i = 0; i < 4; i++) {
		if (check_arr(y + dy[i], x + dx[i])&&arr[y][x]>arr[y+dy[i]][x+dx[i]]) {
			check[dy[i] + y][dx[i] + x] = true;
			res += dfs(y + dy[i], x + dx[i]);
		}
	}
	return memo[y][x] = res;
}

int main() {
	cin >> M >> N;
	for (int y = 0; y < M; y++)
		for (int x = 0; x < N; x++)
			cin >> arr[y][x];

	memset(memo, -1, sizeof(arr));
	memset(check, false, sizeof(check));
	check[0][0] = true;
	memo[M - 1][N - 1] = 1;
	cout << dfs(0, 0);
}