#include <iostream>
#include <vector>
#include <algorithm>
#define LL long long
using namespace std;

LL divide_and_conquer(int start, int end, vector<LL> &arr) {
	if (start == end)
		return arr[start];

	int mid = (start + end) / 2;
	int mid_left = mid;
	int mid_right = mid + 1;

	LL left_side = divide_and_conquer(start, mid_left, arr);
	LL right_side = divide_and_conquer(mid_right, end, arr);

	LL res = max(left_side, right_side);
	LL height = min(arr[mid_left], arr[mid_right]);
	res = max(res, height * 2);

	while (mid_left > start || mid_right < end) {
		//왼쪽 도형을 선택하는 경우
		if (mid_left != start && (mid_right == end || (arr[mid_left-1]>arr[mid_right+1])))
			height = min(height, arr[--mid_left]);
		//오른쪽 도형을 선택하는 경우
		else
			height = min(height, arr[++mid_right]);
		res = max(res, (mid_right - mid_left + 1) * height);
	}
	return res;
}

int main() {
	int N;
	cin >> N;
	vector <LL> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	cout << divide_and_conquer(0, N - 1, arr);
}