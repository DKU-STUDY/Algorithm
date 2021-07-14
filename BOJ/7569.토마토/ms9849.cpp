#include <iostream>
#include <queue>
using namespace std;

typedef struct _Locate{
	int z;
	int y;
	int x;
} Locate;

int map[102][102][102];  // H,N,M순으로 나타냄..
int M, N, H;
int dirX[6] = { 1,-1,0,0,0,0 };
int dirY[6] = { 0,0,1,-1,0,0 };
int dirZ[6] = { 0,0,0,0,1,-1 };
int Min = 0;
queue<Locate> q;

int check() {
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= N; j++) {
			for (int k = 1; k <= M; k++) {
				if (map[i][j][k] == 0) return 1;
			}
		}
	}

	return 0;
}

int main(void) {
	cin >> M >> N >> H;

	for (int k = 1; k <= H; k++) {
		for (int j = 1; j <= N; j++) {
			for (int i = 1; i <= M; i++) {
				cin >> map[k][j][i];

				if (map[k][j][i] == 1)
					q.push({ k,j,i });
			}
		}
	}

	if (check() == 0) { //만약 모든 토마토가 이미 익은상태로 주어졌다면,
		cout << "0";
		return 0;
	}

	while (!q.empty()) {
		Locate l = q.front();
		q.pop();
		for (int i = 0; i < 6; i++) {
			if (l.x + dirX[i] >= 1 && l.x + dirX[i] <= M && l.y + dirY[i] >= 1 && l.y + dirY[i] <= N && l.z + dirZ[i] >= 1 && l.z + dirZ[i] <= H) { // 막혀있는 장소인지, 방문한 정점인지 확인
				if (map[l.z + dirZ[i]][l.y + dirY[i]][l.x + dirX[i]] == 0) { // 배열의 범위를 벗어나는지 확인
					q.push({ l.z + dirZ[i] ,l.y + dirY[i], l.x + dirX[i]});
					map[l.z + dirZ[i]][l.y + dirY[i]][l.x + dirX[i]] = map[l.z][l.y][l.x] + 1;
					if (map[l.z][l.y][l.x] + 1 > Min) Min = map[l.z][l.y][l.x] + 1;
				}	
			}
		}
	}

	if (check() == 1) cout << "-1";
	else cout << Min-1;

	return 0;
}
