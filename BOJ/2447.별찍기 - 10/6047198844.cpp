#include <iostream>
#include <vector>

using namespace std;

void printStar(vector<vector<char>>& arr) {
	int x_size = arr[0].size();
	int y_size = arr.size();

	for (int y = 0; y < y_size; y++) {
		for (int x = 0; x < x_size; x++)
			printf("%c", arr[y][x]);
		printf("\n");
	}

	return;
}

void makeStar(vector<vector<char>>& arr, int y, int x, int size) {
	if (size == 1) {
		arr[y][x] = '*';
		return;
	}

	int resize = size / 3;

	for (int dy = 0; dy < 3; dy++) {
		for (int dx = 0; dx < 3; dx++) {
			if (dy == 1 && dx == 1)
				continue;
			makeStar(arr, y + dy * resize, x + dx * resize, resize);
		}
	}
}


int main() {
	int N;
	cin >> N;
	vector < vector<char>> arr(N, vector<char>(N, ' '));
	makeStar(arr, 0, 0, N);
	printStar(arr);
}