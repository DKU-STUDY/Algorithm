//���� A�� �־����� ��, ���� �� �����ϴ� �κ� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
//
//���� ���, ���� A = { 10, 20, 10, 30, 20, 50 } �� ��쿡 ���� �� �����ϴ� �κ� ������ { 10, 20, 30, 50 } �̰�, ���̴� 4�̴�.

//V[i]���� D[i]�� ���̸� ������ �κ� ������ ������ �ε����� ���Ѵ�.
//D[i]���� A[i]�� ���������� �ϴ� ���� �� ������ ����.
//A[i]���� ������ ���� ���Ѵ�.

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
	// ���� �� ���̸� ������ �ε���
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
