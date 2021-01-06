#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int N;
//N범위 : 1~14
bool arr[15][15];
//y범위 : 1~14  / x범위 : 1~14 

int dy[8] = { -1,-1, 0,+1,+1,+1, 0,-1 };
int dx[8] = { 0,-1,-1,-1, 0,+1,+1,+1 };

void check_Queen(int y, int x, queue<pair<int, int>>& q) {
	if (q.empty()) {
		int check_y;
		int check_x;
		arr[y][x] = !arr[y][x];
		q.push({ y,x });
		for (int i = 0; i < 8; i++) {
			check_y = y;
			check_x = x;
			while (check_y + dy[i] > 0 && check_y + dy[i] <= N && check_x + dx[i] > 0 && check_x + dx[i] <= N) {
				check_y += dy[i];
				check_x += dx[i];
				if (!arr[check_y][check_x]) {
					arr[check_y][check_x] = arr[y][x];
					q.push({ check_y,check_x });
				}
			}
		}
	}
	else {
		while (!q.empty()) {
			int y = q.front().first;
			int x = q.front().second;
			q.pop();
			arr[y][x] = false;
		}
	}

}

int dfs(int y) {
	int res = 0;
	for (int x = 1; x <= N; x++) {
		if (y == N) {
			if (!arr[y][x])
				++res;
			continue;
		}
		if (!arr[y][x]) {
			queue<pair<int, int>> q;
			check_Queen(y, x, q);
			res += dfs(y + 1);
			check_Queen(y, x, q);
		}
	}
	return res;
}

int main() {
	cin >> N;
	memset(arr, false, sizeof(arr));
	cout << dfs(1);
}