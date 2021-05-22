#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//index start���� index end������ ���簢���� ���� ���̰� ū ���簢���� ���Ѵ�.
int divide_and_conquer(int start, int end,vector <int> &fence) {
	if (start == end)
		return fence[start];

	//3���� ���� divide�Ѵ�.
	//���簢���� �߾��� ��ġ�� �ʰ� ���ʿ� �ִ� ���
	//���簢���� �߾��� ��ġ�� ���
	//���簢���� �߾��� ��ġ�� �ʰ� �����ʿ� �ִ� ���
	int mid = (start + end) / 2;
	int left_side = divide_and_conquer(start, mid, fence);
	int right_side = divide_and_conquer(mid + 1, end, fence);
	int res = max(left_side, right_side);
	int left_index = mid;
	int right_index = mid + 1;
	int height = min(fence[left_index], fence[right_index]);
	res = max(res, height * 2);
	while (left_index > start || right_index < end) {
		//left_index�� ���ҽ�Ű�� ���, �� �츦 ���Ǵ°���.
		if ((right_index == end)||left_index > start && fence[left_index-1] > fence[right_index+1]) {
			--left_index;
			height = min(height, fence[left_index]);
		}
		//right_index�� ������Ű�� ���
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