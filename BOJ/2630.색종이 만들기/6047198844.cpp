//분할 정복 알고리즘 연습
/*
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
*/

#include <iostream>

using namespace std;

int paper[128][128];
int white_cnt = 0;
int blue_cnt = 0;

void divide_and_conquer(int from_y, int from_x, int d) {
	bool flag = false;
	int check_arr = paper[from_y][from_x];
	for (int y = from_y; y < from_y + d && !flag; y++) {
		for (int x = from_x; x < from_x + d; x++) {
			if (check_arr != paper[y][x]) {
				flag = !flag;
				break;
			}
		}
	}
	if (flag) {
		divide_and_conquer(from_y, from_x, d / 2);
		divide_and_conquer(from_y, from_x + d / 2, d / 2);
		divide_and_conquer(from_y + d / 2, from_x, d / 2);
		divide_and_conquer(from_y + d / 2, from_x + d / 2, d / 2);
	}
	else {
		if (check_arr)
			blue_cnt++;
		else
			white_cnt++;
	}
	return;
}

int main() {
	int N;
	cin >> N;
	for (int y = 0; y < N; y++)
		for (int x = 0; x < N; x++)
			cin >> paper[y][x];
	divide_and_conquer(0, 0, N);
	cout << white_cnt << "\n" << blue_cnt;
}