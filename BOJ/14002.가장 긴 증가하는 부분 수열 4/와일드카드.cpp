//수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
//
//예를 들어, 수열 A = { 10, 20, 10, 30, 20, 50 } 인 경우에 가장 긴 증가하는 부분 수열은 { 10, 20, 30, 50 } 이고, 길이는 4이다.

//V[i]값은 D[i]의 길이를 가지는 부분 수열중 이전의 인덱스를 말한다.
//D[i]값은 A[i]를 마지막으로 하는 가장 긴 수열의 길이.
//A[i]값은 수열의 값을 말한다.

#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

int v[1001];
int d[1001];
int a[1001];

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
		d[i] = 1;
		v[i] = -1;
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < i; j++) {
			if (a[i] > a[j] && d[i] < d[j] + 1) {
				d[i] = d[j] + 1;
				v[i] = j;
			}
		}
	}

	stack <int> st;
	// 가장 긴 길이를 가지는 인덱스
	int max_idx =  max_element(d, d + N) - d;
	cout << d[max_idx] << "\n";
	st.push(a[max_idx]);
	for (int idx = v[max_idx];idx!=-1;idx = v[idx]) {
		st.push(a[idx]);
	}
	while (!st.empty()) {
		cout << st.top() << " ";
		st.pop();
	}
}
