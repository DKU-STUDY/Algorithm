#include <iostream>
#include <vector>
#define VI vector<int>

using namespace std;

int dp(int x, int y, vector<VI> &memo, vector<VI> &game_board, int end_pos) {
	if (x > end_pos || y > end_pos)
		return 0;
	if (x == end_pos && y == end_pos)
		return 1;

	int& res = memo[y][x];
	if (res != -1)
		return res;

	int cur_pos_value = game_board[y][x];
	return res = dp(x + cur_pos_value, y, memo, game_board, end_pos) || dp(x, y + cur_pos_value, memo, game_board, end_pos);
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<VI> game_board(N, VI(N, 0));
		for (int y = 0; y < N; y++)
			for (int x = 0; x < N; x++)
				cin >> game_board[y][x];
		vector<VI> memo(N, VI(N, -1));
		if (dp(0, 0, memo, game_board, N - 1) != 0) {
			cout << "YES" << "\n";
			continue;
		}
		cout << "NO" << "\n";
	}
}