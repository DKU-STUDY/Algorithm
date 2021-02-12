#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

///미션 : 스택을 이용한다.
// 내가 하려고 하는게 무엇인가.
// 스택을 이용해서 푼다. 구하려는것은 각각의 판자가 만들수있는 최대 사각형의 크기이다.
// 다시말해서 한 판자가 자신을 꼭 포함하면서 만들수있는 최대 사각형의 크기이다.
// 그 말인 즉슨 자신보다 작은 판자가 양옆으로 나오는 순간 최대 사각형의 크기를 구할수있다는 뜻이다.
// 한쪽으로만 나왔을 경우에는 구할수가없다. 한계를 모르기 때문이다.
// 아직 값을 구하지못한 사각형을 스택에 넣는다고 생각하자.

int fence_stack(vector<int> &height) {
	
	height.push_back(0);
	int N = height.size();

	stack <int> st;
	int res = 0;

	for (int idx = 0; idx < N; idx++) {
		//스택이 비엇다는것은 비교가 불가능함을 의미한다.
		//while문은 스택에 남아있는 판자들을 확인하면서 right를 정해줄수있는지 판단한다.
		while (!st.empty()&&height[st.top()]>=height[idx]) {
			int h = height[st.top()];
			st.pop();
			int width = -1;
			if (st.empty()) {
				width = idx;
			}
			else {
				int left = st.top();
				width = idx - left - 1;
			}
			res = max(res, h * width);
		}
		//right값이 정해지지 않았다. 따라서 스택에 넣는다.
		st.push(idx);
	}
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<int> height(N);
		for (int i = 0; i < N; i++)
			cin >> height[i];
		
		cout << fence_stack(height) << "\n";
	}
}