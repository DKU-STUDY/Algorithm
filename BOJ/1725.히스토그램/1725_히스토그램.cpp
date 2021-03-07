#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//index start부터 index end까지의 직사각형중 가장 넒이가 큰 직사각형을 구한다.
int divide_and_conquer(int start, int end,vector <int> &fence) {
	if (start == end)
		return fence[start];

	//3가지 경우로 divide한다.
	//직사각형이 중앙을 걸치지 않고 왼쪽에 있는 경우
	//직사각형이 중앙을 걸치는 경우
	//직사각형이 중앙을 걸치지 않고 오른쪽에 있는 경우
	int mid = (start + end) / 2;
	int left_side = divide_and_conquer(start, mid, fence);
	int right_side = divide_and_conquer(mid + 1, end, fence);
	int res = max(left_side, right_side);
	int left_index = mid;
	int right_index = mid + 1;
	int height = min(fence[left_index], fence[right_index]);
	res = max(res, height * 2);
	while (left_index > start || right_index < end) {
		//left_index를 감소시키는 경우, 좌 우를 살피는것임.
		if ((right_index == end)||left_index > start && fence[left_index-1] > fence[right_index+1]) {
			--left_index;
			height = min(height, fence[left_index]);
		}
		//right_index를 증가시키는 경우
		else {
			++right_index;
			height = min(height, fence[right_index]);
		}
		res = max(res, height * (right_index - left_index + 1));
	}
	return res;
}

int main() {
	int N;
	cin >> N;
	vector <int> fence;
	int num;
	for (int i = 0; i < N; i++) {
		cin >> num;
		fence.push_back(num);
	}
	cout << divide_and_conquer(0, N - 1, fence);
}