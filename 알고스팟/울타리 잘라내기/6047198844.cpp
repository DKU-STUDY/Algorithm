#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;

int divide_and_conquer(int left, int right, vector <int> &board) {
	if (left == right)
		return board[left];

	int mid = (left + right) / 2;
	int res = max(divide_and_conquer(left, mid, board), divide_and_conquer(mid + 1, right, board));

	int lb = mid;
	int rb = mid + 1;
	int height = min(board[lb], board[rb]);
	res = max(res, height * 2);

	while (left < lb || right > rb) {
		if (left == lb || ((rb < right) && (board[lb - 1] < board[rb + 1]))) {
			++rb;
			height = min(height, board[rb]);
		}
		else {
			--lb;
			height = min(height, board[lb]);
		}
		res = max(res, height * (rb - lb + 1));
	}

	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector <int> board;
		int fence;
		while (N--) {
			cin >> fence;
			board.push_back(fence);
		}
		cout << divide_and_conquer(0, board.size() - 1, board) << "\n";
	}
}