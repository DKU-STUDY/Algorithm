#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
	int arr[100][100];
	memset(arr[0], 0, sizeof(int) * 100 * 100);
	int start_x, start_y, end_x, end_y;
	for (int cnt = 0; cnt < 4; cnt++) {
		cin >> start_x >> start_y >> end_x >> end_y;
		for (int x = start_x; x < end_x; x++)
			for (int y = start_y; y < end_y; y++)
				arr[y][x] = 1;
	}
	cout << count(arr[0], arr[0] + 100 * 100, 1);
}
//memset을 주석 처리하면 정답이 아닌데 그 이유??