#include <iostream>
using namespace std;

bool flag = false;

int arr[9][9];
int res[9][9];

void checkArea(const int &y, const int &x, bool* numberCheck) {
	int dy = (y / 3) * 3;
	int dx = (x / 3) * 3;
	
	for (int y = 0; y < 3; y++)
		for (int x = 0; x < 3; x++)
			numberCheck[arr[y + dy][x + dx]] = true;
	return;
}

void checkRow(const int &y, bool *numberCheck) {
	for (int i = 0; i < 9; i++)
		numberCheck[arr[y][i]] = true;
	return;
}

void checkCol(const int &x, bool* numberCheck) {
	for (int i = 0; i < 9; i++)
		numberCheck[arr[i][x]] = true;
	return;
}

//y , x 부터 시작해서 스도쿠를 완성한다.
void dfs(int y, int x) {
	if (flag)
		return;

	if (y == 9) {
		flag = true;
		copy(&arr[0][0], &arr[0][0] + 9 * 9, &res[0][0]);
		return;
	}

	if (arr[y][x]) {
		if (x == 8)
			return dfs(y + 1, 0);
		else
			return dfs(y, x + 1);
	}
		
	bool numberCheck[10]; // 1부터 9까지 있으면 true
	fill_n(numberCheck, 10, false);
	//가로 검사
	checkRow(y, numberCheck);
	//세로 검사
	checkCol(x, numberCheck);
	//네모칸 검사
	checkArea(y, x, numberCheck);

	for (int i = 1; i < 10; i++) {
		if (!numberCheck[i]&&!flag) {
			arr[y][x] = i;
			if (x == 8)
				dfs(y + 1, 0);
			else
				dfs(y, x + 1);
			arr[y][x] = 0;
		}
	}
	return;
}

int main() {
	for (int y = 0; y < 9; y++)
		for (int x = 0; x < 9; x++)
			scanf(" %d", &arr[y][x]);
	dfs(0, 0);
	for (int y = 0; y < 9; y++) {
		for (int x = 0; x < 9; x++) {
			printf("%d ", res[y][x]);
		}
		printf("\n");
	}
}