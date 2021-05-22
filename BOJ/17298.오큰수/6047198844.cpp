#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int N;
	cin >> N;
	int num; 
	vector <int> vt;
	for (int i = 0; i < N; i++) {
		cin >> num;
		vt.push_back(num);
	}

	vector <int> res;
	res.resize(vt.size());
	stack <int> st;
	for (int i = 0; i < N; i++) {
		if (!st.empty()) {
			while (!st.empty()&&vt[st.top()] < vt[i]) {
				res[st.top()] = vt[i];
				st.pop();
			}
		}
		st.push(i);
	}
	for (int i = 0; i < N; i++) {
		if (res[i])
			cout << res[i] << " ";
		else
			cout << "-1" << " ";
	}
}