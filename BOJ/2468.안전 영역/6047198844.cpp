#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

int board[100][100];
bool board_01[100][100];

//ÁÂ¿ì»óÇÏ
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
bool range(int n, int y, int x) {
	if (0 > y || y >= n)
		return false;
	if (0 > x || x >= n)
		return false;
	return true;
}

int bfs(int under_value,int n) {
	for (int y = 0; y < n; y++)
		for (int x = 0; x < n; x++)
				board_01[y][x] = board[y][x] <= under_value ? false : true;
	
	int cnt = 0;
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++) {
			if (board_01[y][x]) {
				cnt++;
				queue <pair<int,int> > q;
				q.push({ y,x });
				while (!q.empty()) {
					int y = q.front().first;
					int x = q.front().second;
					q.pop();
					for (int di = 0; di < 4; di++) {
						int check_y = dy[di] + y;
						int check_x = dx[di] + x;
						if (range(n,check_y,check_x)&&board_01[check_y][check_x]) {
							q.push({ check_y,check_x });
							board_01[check_y][check_x] = false;
						}
					}
				}
			}
		}
	}
	return cnt;
}

int main() {
	int n;
	cin >> n;
	int max_value = 0;
	for (int y = 0; y < n; y++)
		for (int x = 0; x < n; x++) {
			cin >> board[y][x];
			max_value = max(board[y][x], max_value);
		}
	int res_result = 0;
	for (int i = 0; i <= max_value; i++) {
		res_result = max(res_result, bfs(i,n));
	}
	cout << res_result;
}