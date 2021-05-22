#include <iostream>
#include <vector>

using namespace std;

//상 하 좌 우
int dy[4] = { -1,+1, 0, 0 };
int dx[4] = { 0, 0,-1,+1 };

void dfs(int x,int y, int xSize, int ySize , vector<vector<int>> &arr) {
	--arr[y][x];
	int y_size = arr.size();
	int x_size = arr[0].size();

	for (int d = 0; d < 4; d++) {
		int y_ = y + dy[d]; int x_ = x + dx[d];
		if ((0 <= y_ && y_ < y_size) &&
			(0 <= x_ && x_ < x_size) &&
			arr[y_][x_])
			dfs(x_, y_, xSize, ySize, arr);
	}
	return;
}

int dfs_all(vector<vector<int>> &arr) {
	int res = 0;
	int ySize = arr.size();
	int xSize = arr[0].size();
	for (int y = 0; y < ySize; y++)
		for (int x = 0; x < xSize; x++)
			if (arr[y][x]) { dfs(x, y, xSize, ySize, arr); res++; }
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int M, N;
		cin >> M >> N;
		vector<vector<int>> arr(N, vector<int>(M, 0));
		int K;
		cin >> K;
		int x, y;
		while (K--) {
			cin >> x >> y;
			arr[y][x] = 1;
		}
		cout << dfs_all(arr) << "\n";
	}
}