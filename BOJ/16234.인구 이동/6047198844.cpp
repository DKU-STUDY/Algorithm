#include <iostream>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

const int dy[4] = { -1,+1,0,0 };
const int dx[4] = { 0,0,-1,+1 };

bool rangeCheck(int y, int x, int N) {
	if (0 <= y && y < N &&
		0 <= x && x < N)
		return true;
	return false;
}

int bfs(vector<vector<int>> arr,int N,int L, int R) {
	int cnt = 0;
	while (1) {
		bool flag = false;
		vector < vector < bool >> check(N, vector<bool>(N));
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				if (!check[y][x]) {
					queue <pair<int, int>> q;
					queue <pair<int, int>> cq;
					check[y][x] = true;
					q.push({ y,x });

					int sum = arr[y][x];
					while (!q.empty()) {
						int y = q.front().first;
						int x = q.front().second;
						q.pop();

						for (int d = 0; d < 4; d++) {
							int iy = y + dy[d];
							int ix = x + dx[d];
							if (rangeCheck(iy, ix, N) && !check[iy][ix]) {
								int sub = abs(arr[y][x] - arr[iy][ix]);
								if (L <= sub && sub <= R) {
									q.push({ iy,ix });
									cq.push({ iy,ix });
									sum += arr[iy][ix];
									check[iy][ix] = true;
								}
							}
						}
					}
					int avg;
					if (cq.size()) {
						cq.push({ y,x });
						avg = sum / cq.size();
						flag = true;
					}
					while (!cq.empty()) {
						int y = cq.front().first;
						int x = cq.front().second;
						cq.pop();
						arr[y][x] = avg;
					}
				}
			}
		}
		if (flag)
			cnt++;
		else
			return cnt;
	}
}

int main() {
	int N, L, R;
	cin >> N >> L >> R;
	vector<vector<int>> arr(N, vector<int>(N));
	for (int y = 0; y < N; y++)
		for (int x = 0; x < N; x++)
			cin >> arr[y][x];
	cout << bfs(arr, N, L, R);
}