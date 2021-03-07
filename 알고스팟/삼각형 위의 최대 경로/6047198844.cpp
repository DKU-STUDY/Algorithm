#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp(int y, int x,int N, vector <vector<int>> &triangle, vector <vector<int>>& memo) {
	if (y == N - 1)
		return triangle[y][x];
	
	int& res = memo[y][x];
	if (res != -1)
		return res;

	return res = triangle[y][x] + max(dp(y + 1, x, N, triangle, memo), dp(y + 1, x + 1, N, triangle, memo));
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector <vector<int>> triangle(N, vector<int>(N));
		vector <vector<int>> memo(N, vector<int>(N, -1));
		for (int y = 0; y < N; y++) {
			for (int x = 0; x <= y; x++) {
				cin >> triangle[y][x];
			}
		}
		cout << dp(0, 0, N, triangle, memo) << "\n";
	}
	
}