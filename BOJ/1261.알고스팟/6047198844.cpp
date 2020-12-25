#include <iostream>
#include <queue>
using namespace std;

int arr[100][100]; // 그냥값
pair <int,bool> arr_sum_bool[100][100]; // 누적값 / 방문했는지
int around[4][2] = { {1,0}, {-1,0}, {0,-1}, {0,1} }; // 상하좌우
int M; int N; // x값 ,y값

bool Range(int y, int x) {
	if (x < 0 || x >= M)
		return false;
	if (y < 0 || y >= N)
		return false;
	return true;
}

int bfs(){
	queue <pair<int, int>> q; // y값 x값
	q.push(make_pair(0, 0)); 
	arr_sum_bool[0][0].first = 0; arr_sum_bool[0][0].second = true;
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++){
			int pushed_y = y + around[i][0];
			int pushed_x = x + around[i][1];
			if (Range(pushed_y, pushed_x)){
				if (!arr_sum_bool[pushed_y][pushed_x].second){
					q.push(make_pair(pushed_y, pushed_x));
					arr_sum_bool[pushed_y][pushed_x].second = true;
					if (arr_sum_bool[pushed_y][pushed_x].first > arr_sum_bool[y][x].first + arr[y][x]) {
						arr_sum_bool[pushed_y][pushed_x].first = arr_sum_bool[y][x].first + arr[y][x];
					}
				}
				else {
					if (arr_sum_bool[pushed_y][pushed_x].first > arr_sum_bool[y][x].first + arr[y][x]) {
						q.push(make_pair(pushed_y, pushed_x));
						arr_sum_bool[pushed_y][pushed_x].first = arr_sum_bool[y][x].first + arr[y][x];
					}
				}
				
					
			}
		}
	}

	return arr_sum_bool[N - 1][M - 1].first;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> M >> N;

	for (int y = 0; y < N; y++)for (int x = 0; x < M; x++)
		scanf(" %1d", &arr[y][x]);

	for (int y = 0; y < N; y++)for (int x = 0; x < M; x++)
	{
		arr_sum_bool[y][x].first = 999999;
		arr_sum_bool[y][x].second = false;
	}

	cout << bfs();
}