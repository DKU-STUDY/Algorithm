//폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
//
//정사각형은 서로 겹치면 안 된다.
//도형은 모두 연결되어 있어야 한다.
//정사각형의 변끼리 연결되어 있어야 한다.즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
//정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
//
//아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다.종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
//
//테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
//
//테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
/*
	1. 각각의 경우의 수를 구한다
		테트로미노는 19가지의 경우의 수가 있다.
		각각 가장 좌상단의 정사각형은 N X M 칸정도 가능하다.
		N = 4 M = 500 이므로 4*500*19 < 1억
		따라서 브루트 포스로 가능하다.

	2. 가능한 모든 방법을 다 만들어 본다.
		각각의 경우의 수를 프로그래밍한다.

*/
#include <iostream>
#include <vector>
using namespace std;

//19개의 테트로미노를 만든다. 좌상단 기준. y증가량, x증가량
vector <pair<int, int>> tetromino[19] = {
	{{0,0},{0,1},{0,2},{0,3}},
	{{0,0},{1,0},{2,0},{3,0}},
	{{0,0},{0,1},{1,0},{1,1}},
	{{0,0},{1,0},{2,0},{1,1}},
	{{0,0},{0,1},{1,1},{0,2}},
	{{0,0},{-1,1},{0,1},{1,1}},
	{{0,0},{-1,1},{0,1},{0,2}},
	{{0,0},{0,1},{0,2},{1,2}},
	{{0,0},{1,0},{2,0},{0,1}},
	{{0,0},{1,0},{1,1},{1,2}}, 
	{{0,0},{-2,1},{-1,1},{0,1}},
	{{0,0},{1,0},{0,1},{0,2}},
	{{0,0},{0,1},{1,1},{2,1}},
	{{0,0},{0,1},{-1,2},{0,2}},
	{{0,0},{1,0},{2,0},{2,1}},
	{{0,0},{0,1},{-1,1},{-1,2}},
	{{0,0},{1,0},{1,1},{2,1}},
	{{0,0},{0,1},{1,1},{1,2}},
	{{0,0},{1,0},{0,1},{-1,1}},
};

int arr[501][501];
int N; int M;
int brute_force() {
	//테트로미노 19개를 좌상단을 기준으로 N X M 배열에 모두 놓는다. 1,1부터 시작. 500,500까지
	//각 좌표중 하나라도 1미만이거나 N초과일경우 답에 해당되지 않는다.
	int max = 0; int res = 0;
	for (int i = 0; i < 19; i++) {

		for (int y = 1; y <= N; y++) for (int x = 1; x <= M; x++) {
			if ((y + tetromino[i][0].first >= 1 && y + tetromino[i][0].first <= N)&&(x + tetromino[i][0].second >= 1 && x + tetromino[i][0].second <= M)&&
				(y + tetromino[i][1].first >= 1 && y + tetromino[i][1].first <= N)&&(x + tetromino[i][1].second >= 1 && x + tetromino[i][1].second <= M) &&
				(y + tetromino[i][2].first >= 1 && y + tetromino[i][2].first <= N)&&(x + tetromino[i][2].second >= 1 && x + tetromino[i][2].second <= M) &&
				(y + tetromino[i][3].first >= 1 && y + tetromino[i][3].first <= N)&&(x + tetromino[i][3].second >= 1 && x + tetromino[i][3].second <= M)
				) {
				res = arr[y + tetromino[i][0].first][x + tetromino[i][0].second] +
					arr[y + tetromino[i][1].first][x + tetromino[i][1].second] +
					arr[y + tetromino[i][2].first][x + tetromino[i][2].second] +
					arr[y + tetromino[i][3].first][x + tetromino[i][3].second];
				max = max > res ? max : res;
			}
		}
	}

	return max;
}
int main() {

	cin >> N >> M;
	for (int y = 1; y <= N; y++) for (int x = 1; x <= M; x++) {
		cin >> arr[y][x];
	}
	cout << brute_force();
}