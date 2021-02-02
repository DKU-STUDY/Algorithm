#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int maxPathMemo[100][100];
int pathNumMemo[100][100];
int path[100][100];

//n은 최대 y값.
int MaxPath(int y, int x,int n) {
	int &res = maxPathMemo[y][x];
	if (y == n)
		return path[y][x];
	if (res != -1)
		return res;
	return res = path[y][x] + max(MaxPath(y + 1, x, n), MaxPath(y + 1, x + 1, n));
}

int PathNum(int y, int x,int n) {
	int& res = pathNumMemo[y][x];
	if (y == n)
		return 1;
	if (res != -1)
		return res;

	int leftMaxPath = MaxPath(y + 1, x, n);
	int RightMaxPath = MaxPath(y + 1, x + 1, n);

	if (leftMaxPath == RightMaxPath)
		return res = PathNum(y + 1, x, n) + PathNum(y + 1, x + 1, n);
	else if (leftMaxPath > RightMaxPath)
		return res = PathNum(y + 1, x, n);
	else
		return res = PathNum(y + 1, x + 1, n);
}

int main() {
	int C;
	cin >> C;
	int n;
	while (C--) {
		memset(maxPathMemo, -1, sizeof(maxPathMemo));
		memset(pathNumMemo, -1, sizeof(pathNumMemo));
		memset(path, -1, sizeof(path));
		cin >> n;
		for (int y = 0; y < n; y++) {
			for (int x = 0; x <= y; x++) {
				cin >> path[y][x];
			}
		}
		cout << PathNum(0, 0, n - 1) << "\n";
	}
}