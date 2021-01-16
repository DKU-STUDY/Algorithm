#include <iostream>
#include <cstring>

using namespace std;

int board_y;
int board_x;
bool check[50][50];
char board[50][50];
int dy[4] = {0,0,-1,+1};
int dx[4] = {-1,+1,0,0};

bool dfs(int y, int x, int start_y, int start_x,int cnt) {

	if (check[y][x]) {
		if ((y == start_y) && (x == start_x) && cnt >= 4) {
			return true;
		}
		return false;
	}
	check[y][x] = true;
	
	for (int i = 0; i < 4; i++) {
		if ((y < 0 || y >= board_y) || (x < 0 || x >= board_x))
			continue;
		if (board[y][x] == board[y + dy[i]][x + dx[i]])
			if (dfs(y + dy[i], x + dx[i], start_y, start_x, cnt + 1))
				return true;
	}
	return false;
}

int main() {
	cin >> board_y >> board_x;
	for (int y = 0; y < board_y; y++)
		for (int x = 0; x < board_x; x++)
			cin >> board[y][x];

	for (int y = 0; y < board_y; y++)
		for (int x = 0; x < board_x; x++) {
			if (dfs(y, x, y, x, 0)) {
				cout << "Yes";
				return 0;
			}
			memset(check, false, sizeof(check));
		}
	cout << "No";
}