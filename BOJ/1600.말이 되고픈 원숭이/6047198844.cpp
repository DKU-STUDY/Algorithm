#include <iostream>
#include <queue>

using namespace std;

int board[200][200][31];

int dy[4] = {0,0,-1,1};
int dx[4] = {-1,1,0,0};
int horse_dy[8] = {-1,-2,-2,-1,1,2, 2, 1};
int horse_dx[8] = {-2,-1, 1, 2,2,1,-1,-2};
bool range(int W,int H, int y, int x) {
	if (0 > y || y >= H)
		return false;
	if (0 > x || x >= W)
		return false;
	return true;
}

int bfs(int W,int H,int K) {
	if (W == 1 && H == 1)
		return 0;
	pair <pair<int, int>, int> start = { {0,0},K };
	queue < pair <pair<int, int>, int>> q;
	q.push(start);
	for(int i=0;i<=K;i++)
		board[0][0][i] = 1;
	int res = 0;
	while (!q.empty()) {
		int cnt = q.size();
		while (cnt--) {
			int y = q.front().first.first;
			int x = q.front().first.second;
			int k = q.front().second;
			q.pop();
			if (y == H - 1 && x == W - 1)
				return res;
			//상하좌우
			for (int i = 0; i < 4; i++) {
				int check_y = y + dy[i];
				int check_x = x + dx[i];
				if (range(W, H, check_y, check_x) && !board[check_y][check_x][k]) {
					q.push({ { check_y,check_x }, k });
					board[check_y][check_x][k] = 1;
				}
			}

			//말로 움직일수있나 판단
			if (k) {
				--k;
				for (int i = 0; i < 8; i++) {
					int check_y = y + horse_dy[i];
					int check_x = x + horse_dx[i];
					if (range(W, H, check_y, check_x) && !board[check_y][check_x][k]) {
						q.push({ { check_y,check_x }, k });
						board[check_y][check_x][k] = 1;
					}
				}
			}
		}
		res++;
	}
	return -1;
}


int main() {
	int K;
	cin >> K;
	int W; int H;
	cin >> W >> H;
	for (int y = 0; y < H; y++)
		for (int x = 0; x < W; x++) {
			cin >> board[y][x][0];
			for (int i = 1; i <= K; i++)
				board[y][x][i] = board[y][x][0];
		}
	cout << bfs(W,H,K);
}