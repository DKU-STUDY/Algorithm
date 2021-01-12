#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>

using namespace std;

int arr[126][126];
int memo[126][126];

int dy[4] = { -1,+1,0,0 };
int dx[4] = { 0,0,-1,+1 };

bool range_check(int x, int y, int n) {
	if (x < 0 || x >= n)
		return false;
	if (y < 0 || y >= n)
		return false;
	return true;
}

int Dijkstra(int N) {
	priority_queue <pair<int, pair<int, int> > > pq;
	pq.push({ -arr[0][0], { 0,0 } });
	memo[0][0] = arr[0][0];
	while (!pq.empty()) {
		int here_y = pq.top().second.first;
		int here_x = pq.top().second.second;
		int here_cost = -pq.top().first;
		pq.pop();
		if (here_y == N - 1 && here_x == N - 1)
			return here_cost;
		for (int i = 0; i < 4; i++) {
			int there_y = here_y + dy[i];
			int there_x = here_x + dx[i];
			if (range_check(there_y, there_x,N)) {
				int there_cost = arr[there_y][there_x];
				if (memo[there_y][there_x] == -1 ||
					memo[there_y][there_x] > here_cost + there_cost) {
					memo[there_y][there_x] = here_cost + there_cost;
					pq.push({ -(here_cost + there_cost),{there_y,there_x} });
				}
			}
		}
	}
}

int main() {
	int N = -1;
	for (int cnt = 1; N != 0; cnt++) {
		cin >> N;
		if (N == 0)
			return 0;
		memset(memo, -1, sizeof(memo));
		for (int y = 0; y < N; y++)
			for (int x = 0; x < N; x++)
				cin >> arr[y][x];
		cout << "Problem " << cnt << ": " << Dijkstra(N) << "\n";
	}
}